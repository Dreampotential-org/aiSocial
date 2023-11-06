import logging
from django.http import JsonResponse
from db_connection import collection
# from twilio.twiml.voice_response import VoiceResponse
from django.http import HttpResponse
from django.http import JsonResponse
from twilio.rest import Client
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import requests
import time

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        self.logger.info(f"Path: {request.path}, Method: {request.method}, User: {request.user}")

        if request.path == '/make-calls/' and request.method == 'POST':
            phone_number = request.POST.get('phone')
            start_time = time.time()
            self.logger.info(f"Phone Number: {phone_number}, Request Start Time: {start_time}")

            response = self.get_response(request)

            end_time = time.time()
            self.logger.info(f"Phone Number: {phone_number}, Request End Time: {end_time}")
            
            return response
        else:
            response = self.get_response(request)
            return response