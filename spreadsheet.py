
''' ###################################
-- if service_account.json is in project directory, use:
sa = gspread.service_account(filename='service_account.json')
###################################'''

import gspread
import pandas as pd
import translate
import send_sms

#open the document
sa = gspread.service_account()
sh = sa.open("AutomatedSystem TestSheet")
wks = sh.worksheet("Sheet1")
d = wks.get_all_records()
df = pd.DataFrame(data=d)

#global variables
col_to_letter = {}
patient_data = {}

#print(df.columns)
def add_to_dict():
    starting_col = 65
    for c in df.columns:
        col_to_letter[c] = chr(starting_col)
        starting_col += 1
add_to_dict()

def add_to_patient_data():
    i = 2
    for data in d:
        patient_data[i] = data
        i += 1
add_to_patient_data()

for id in patient_data:
    name = patient_data[id]['Patient Name (Last, first)']
    message = patient_data[id]["Message"]
    language = patient_data[id]["Language"]
    phone = str(patient_data[id]["Phone #"])
    lang_code = translate.languages(language)
    translated = translate.translate_text(lang_code, message)
    wks.update(col_to_letter["Translated Message"]+str(id), translated)
    patient_data[id]["Translated Message"] = translated
    #print(name, message, "+1"+phone)

for i in patient_data:
    unique_id = i
    name = patient_data[unique_id]["Patient Name (Last, first)"].split((", "))
    first, last = name[1], name[0]
    m = patient_data[unique_id]["Message"]
    daytime = patient_data[unique_id]["Day/Time of Scheduling"]
    appointment_time = patient_data[unique_id]["Appointment Time"]
    mess = "Hello "+first+" "+last+", \n"+"You have an appointment at Paul Hom Asian Clinic on "+daytime+" "+appointment_time+". Call 4088052770 to CANCEL or RESCHEDULE. \n"
    language = patient_data[unique_id]["Language"]
    lang_code = translate.languages(language)
    tr_mess = translate.translate_text(lang_code, mess)
    p = patient_data[unique_id]["Phone #"]
    mess = mess+"************\n"+tr_mess
    print(mess)
    send_sms.send_text(mess, p)



#df = pd.DataFrame(data = d,columns=["Appointment Time", "Language", "Phone #"])
#print(df)
#wks.update('A2', 'need to reschedule')

