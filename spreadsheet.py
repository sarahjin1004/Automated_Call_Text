
''' ###################################
-- service_account.json is in ~/.config/gspread
-- if service_account.json is in project directory, use:
sa = gspread.service_account(filename='service_account.json')
###################################'''

import gspread


sa = gspread.service_account()
sh = sa.open("AutomatedSystem TestSheet")

wks = sh.worksheet("Sheet1")

print(wks.acell('C2').value)
print(wks.get_all_records())
wks.update('A2', 'no show')

