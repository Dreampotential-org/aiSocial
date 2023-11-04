import os
from django.core.management.base import BaseCommand
from django.http import JsonResponse
from twilio.rest import Client
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import requests
import time
from db_connection import collection





class Command(BaseCommand):
    help = 'Import address extra'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):


    
        account_sid = settings.TWILIO['TWILIO_ACCOUNT_SID']
        auth_token = settings.TWILIO['TWILIO_AUTH_TOKEN']
        twilio_number = settings.TWILIO['TWILIO_PHONE_NUMBER']

        client = Client(account_sid, auth_token)

        # Fetch phone numbers from the API
        # response = requests.get('http://127.0.0.1:8000/get-all-phones/')  # Replace with your API URL
        all_phones = list(collection.find({}, {'_id': 0, 'phone': 1}))

        # all_phones = response.json()

        call_data = []

        for phone_data in all_phones:
            phone_number = '+91' + phone_data.get('phone')  # Adding the country code to the phone number

            # Make a call for each phone number
            call = client.calls.create(
                to=phone_number,
                from_=twilio_number,
                url='http://demo.twilio.com/docs/voice.xml'  # A TwiML URL or a TwiML Bin URL
            )

            time.sleep(15)  # Adjust the sleep time as needed

            call = client.calls(call.sid).fetch()

            if call.status == 'in-progress' and call.duration is None:
                call_status = 'not-answered'  # Call was not answered
            else:
                call_status = call.status  # Call status is either 'completed' or 'in-progress'

            call_info = {
                'phone_number': phone_number,
                'call_sid': call.sid,
                'call_status': call_status
            }

            call_data.append(call_info)

        response_data = {
            'message': 'Calls initiated successfully',
            'call_data': call_data
        }



