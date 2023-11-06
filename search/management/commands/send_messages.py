import os
from django.core.management.base import BaseCommand
from twilio.rest import Client
from django.conf import settings

class Command(BaseCommand):
    help = 'Send Twilio messages'

    def handle(self, *args, **options):
        twilio_account_sid = settings.TWILIO['TWILIO_ACCOUNT_SID']
        twilio_auth_token = settings.TWILIO['TWILIO_AUTH_TOKEN']
        twilio_phone_number = settings.TWILIO['TWILIO_PHONE_NUMBER']

        print(f"Twilio Account SID: {twilio_account_sid}")
        print(f"Twilio Auth Token: {twilio_auth_token}")
        print(f"Twilio Phone Number: {twilio_phone_number}")

        client = Client(twilio_account_sid, twilio_auth_token)

        def send_message(to, body):
            try:
                message = client.messages.create(
                    body=body,
                    from_=twilio_phone_number,
                    to=to
                )
                print(f"Message sent successfully. Message SID: {message.sid}")
            except Exception as e:
                print(f"Error sending message: {e}")

        to_number = '+18434259777'  

        message_body = 'Hello from Twilio!'

        send_message(to_number, message_body)
