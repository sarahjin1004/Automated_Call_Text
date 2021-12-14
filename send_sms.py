# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import translate

#translated_message = translate.translate_text("ko", "hello")

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def send_text(message, caller):
    message = client.messages \
                    .create(
                        body=message,
                        from_=os.environ['TWILIO_PHONE'],
                        to=caller
                    )

#send_text()
