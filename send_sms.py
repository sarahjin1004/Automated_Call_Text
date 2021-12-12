# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import translate

t = translate.translate_text("ko", "hello")

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=t[1],
                     from_='+12693672928',
                     to=os.environ['RECEIVER_PHONE']
                 )

print(message.sid)
