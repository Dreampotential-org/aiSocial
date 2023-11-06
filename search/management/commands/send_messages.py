import os
from django.core.management.base import BaseCommand
from twilio.rest import Client
from django.conf import settings


def send_message(client, to, body):
    twilio_phone_number = settings.TWILIO['TWILIO_PHONE_NUMBER']
    message = client.messages.create(
        body=body,
        from_=twilio_phone_number,
        to=to
    )
    print(message)
    print(f"Message sent successfully. Message SID: {message.sid}")


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

        to_number = '+16468300399'  
        message_body = 'Hello from Twilio!'
        send_message(client, to_number, message_body)
