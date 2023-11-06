from django.http import JsonResponse
from db_connection import collection
# from twilio.twiml.voice_response import VoiceResponse
from django.http import HttpResponse

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
from bson import ObjectId

# twilio_app/views.py
@csrf_exempt
def delete_data(request, data_id):
    if request.method == 'DELETE':
        try:
            # Delete data based on the provided ID
            delete_result = collection.delete_one({'_id': ObjectId(data_id)})

            if delete_result.deleted_count == 1:
                response_data = {
                    'message': f'Data with ID {data_id} deleted successfully'
                }
                return JsonResponse(response_data, status=200)
            else:
                error_response = {
                    "error": {
                        "type": "DATA-NOT-FOUND",
                        "code": "404",
                        "message": f"Data with ID {data_id} not found"
                    }
                }
                return JsonResponse(error_response, status=404)

        except Exception as e:
            error_response = {
                "error": {
                    "type": "SERVER-ERROR",
                    "code": "500",
                    "message": "Internal Server Error - " + str(e)
                }
            }
            return JsonResponse(error_response, status=500)
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
            # Twilio client setup
            account_sid = settings.TWILIO['TWILIO_ACCOUNT_SID']
            auth_token = settings.TWILIO['TWILIO_AUTH_TOKEN']
            twilio_number = settings.TWILIO['TWILIO_PHONE_NUMBER']
            client = Client(account_sid, auth_token)

            # Fetch phone numbers from the API
            response = requests.get('http://127.0.0.1:8000/get-all-phones/')  # Replace with your API URL
            all_phones = response.json()

            call_data = []

            for phone_data in all_phones:
                phone_number = '+91' + phone_data.get('phone')

                # Make a call for each phone number
                call = client.calls.create(
                    to=phone_number,
                    from_=twilio_number,
                    url='http://demo.twilio.com/docs/voice.xml'  # A TwiML URL or a TwiML Bin URL
                )
                print(call.__dict__)  # Print the call object to inspect its attributes

                call_info = {
                    'phone_number': phone_number,
                    'call_sid': call.sid,
                    'start_time': call.start_time,  # Logging the start time
                    'end_time': call.end_time,  # Logging the end time
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
    else:
        return HttpResponse(status=405)

# Webhook endpoint to handle call status updates
@csrf_exempt
def webhook_endpoint(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        print("Received webhook data:")
        print(payload)

        call_sid = payload.get('CallSid')
        call_status = payload.get('CallStatus')
        call_duration = payload.get('CallDuration')

        # Store or log the call status and duration here for later use

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)
# from twilio.rest import Client

from twilio.twiml.voice_response import VoiceResponse, Gather, Dial, Pause, Number,Record,Say
from twilio.twiml.voice_response import VoiceResponse

SERVER_URL = 'https://py-api.dreampotential.org'

@csrf_exempt
def handle_incoming_call(request):
    print("Handle incoming call has been called")
    response = VoiceResponse()
    dial = Dial(
        record='record-from-ringing-dual',
        timeout="1000",
    )
    dial.number('+18434259777')
    response.append(dial)
    response.say("Hi, I can't come to the phone right now, please leave a message after the beep",voice="alice")
    response.record(
        recording_status_callback=SERVER_URL + '/voip/api_voip/recording_status_callback',
        recording_status_callback_event='completed')
    response.hangup()
    return HttpResponse(response)


@csrf_exempt
def recording_status_callback(request):
    print("Handle recording status callback")
    data = request.POST
    print(data)
    return HttpResponse("")



@csrf_exempt
def twilio_call_status(request):
    print("twilio call status called %s" % request.method)
    data = request.POST
    print(data)

    return JsonResponse({"success":True})


from django.conf import settings
from django.http import JsonResponse
from twilio.rest import Client
@csrf_exempt
def send_message_view(request):
    if request.method == 'POST':
        try:
            # Twilio client setup
            account_sid = settings.TWILIO['TWILIO_ACCOUNT_SID']
            auth_token = settings.TWILIO['TWILIO_AUTH_TOKEN']
            twilio_number = settings.TWILIO['TWILIO_PHONE_NUMBER']
            client = Client(account_sid, auth_token)

            # Phone number to send the message to
            to_number = '+18434259777'  # Replace with the desired phone number

            # Send the message using Twilio
            message = client.messages.create(
                body='nadeeem here ',  # Replace with your desired message
                from_=twilio_number,
                to=to_number
            )

            response_data = {
                'message': 'Message sent successfully',
                'message_sid': message.sid
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

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
