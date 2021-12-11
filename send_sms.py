# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#account_sid = os.environ['TWILIO_ACCOUNT_SID']
account_sid = 'ACdb0749096a5c2ee4b61459b3a1ce6ea9'
#auth_token = os.environ['TWILIO_AUTH_TOKEN']
auth_token = '616986aa39f31924281a98e424e3502a'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Testing from Automated_Call_Text.",
                     from_='+12693672928',
                     to='+14088052770'
                 )

print(message.sid)