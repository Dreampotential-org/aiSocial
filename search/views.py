from django.http import JsonResponse
from db_connection import collection
# from django.db import models

# from twilio.twiml.voice_response import VoiceResponse

# Function to get all data
def get_all_data(request):
    if request.method == 'GET':
        try:
            all_data = list(collection.find({}, {'_id': 0}))
            return JsonResponse(all_data, safe=False)

        except Exception as e:
            error_response = {
                "error": {
                    "type": "SERVER-ERROR",
                    "code": "500",
                    "message": "Internal Server Error - " + str(e)
                }
            }
            return JsonResponse(error_response, status=500)

# Function to get all names
def get_all_names(request):
    if request.method == 'GET':
        try:
            all_names = list(collection.find({}, {'_id': 0, 'name': 1}))
            return JsonResponse(all_names, safe=False)

        except Exception as e:
            error_response = {
                "error": {
                    "type": "SERVER-ERROR",
                    "code": "500",
                    "message": "Internal Server Error - " + str(e)
                }
            }
            return JsonResponse(error_response, status=500)

# Function to get all states
def get_all_states(request):
    if request.method == 'GET':
        try:
            all_states = list(collection.find({}, {'_id': 0, 'state': 1}))
            return JsonResponse(all_states, safe=False)

        except Exception as e:
            error_response = {
                "error": {
                    "type": "SERVER-ERROR",
                    "code": "500",
                    "message": "Internal Server Error - " + str(e)
                }
            }
            return JsonResponse(error_response, status=500)

# Function to get all emails
def get_all_emails(request):
    if request.method == 'GET':
        try:
            all_emails = list(collection.find({}, {'_id': 0, 'email': 1}))
            return JsonResponse(all_emails, safe=False)

        except Exception as e:
            error_response = {
                "error": {
                    "type": "SERVER-ERROR",
                    "code": "500",
                    "message": "Internal Server Error - " + str(e)
                }
            }
            return JsonResponse(error_response, status=500)

# Function to get all phones
def get_all_phones(request):
    if request.method == 'GET':
        try:
            all_phones = list(collection.find({}, {'_id': 0, 'phone': 1}))
            return JsonResponse(all_phones, safe=False)

        except Exception as e:
            error_response = {
                "error": {
                    "type": "SERVER-ERROR",
                    "code": "500",
                    "message": "Internal Server Error - " + str(e)
                }
            }
            return JsonResponse(error_response, status=500)

# Function to get all Solds
def get_all_solds(request):
    if request.method == 'GET':
        try:
            all_solds = list(collection.find({}, {'_id': 0, 'Solds': 1}))
            return JsonResponse(all_solds, safe=False)

        except Exception as e:
            error_response = {
                "error": {
                    "type": "SERVER-ERROR",
                    "code": "500",
                    "message": "Internal Server Error - " + str(e)
                }
            }
            return JsonResponse(error_response, status=500)
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Extract data from the request
            name = data.get('name')
            state = data.get('state')
            email = data.get('email')
            phone = data.get('phone')
            Solds = data.get('Solds')

            # Create a dictionary for the new user
            new_user = {
                'name': name,
                'state': state,
                'email': email,
                'phone': phone,
                'Solds': Solds
            }

            # Insert the new user into the MongoDB collection
            collection.insert_one(new_user)

            # Prepare the response data
            response_data = {
                'message': 'User added successfully'
            }

            return JsonResponse(response_data, status=201)

        except Exception as e:
            error_response = {
                "error": {
                    "type": "SERVER-ERROR",
                    "code": "500",
                    "message": "Internal Server Error - " + str(e)
                }
            }
            return JsonResponse(error_response, status=500)

# twilio_app/views.py

from django.http import JsonResponse
from twilio.rest import Client
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import requests
import time

@csrf_exempt
def make_calls(request):
    if request.method == 'POST':
        try:
            account_sid = settings.TWILIO['TWILIO_ACCOUNT_SID']
            auth_token = settings.TWILIO['TWILIO_AUTH_TOKEN']
            twilio_number = settings.TWILIO['TWILIO_PHONE_NUMBER']

            client = Client(account_sid, auth_token)

            # Fetch phone numbers from the API
            response = requests.get('http://127.0.0.1:8000/get-all-phones/')  # Replace with your API URL
            all_phones = response.json()

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

            return JsonResponse(response_data, status=200)

        except Exception as e:
            error_response = {
                "error": {
                    "type": "TWILIO-ERROR",
                    "code": "500",
                    "message": "Twilio Error - " + str(e)
                }
            }
            return JsonResponse(error_response, status=500)