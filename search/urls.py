# search/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Other paths
    path('api/get_all_data/', views.get_all_data, name='get_all_data'),
    path('api/create_user/', views.create_user, name='create_user'),
    path('get-all-names/', views.get_all_names, name='get_all_names'),
    path('get-all-states/', views.get_all_states, name='get_all_states'),
    path('get-all-emails/', views.get_all_emails, name='get_all_emails'),
    path('get-all-phones/', views.get_all_phones, name='get_all_phones'),
    path('get-all-solds/', views.get_all_solds, name='get_all_solds'),
    # path('delete-data/<int:id>/', views.delete_data, name='delete_data'),
    path('delete-data/<str:data_id>', views.delete_data, name='delete_data'),
    path('webhook-endpoint/', views.webhook_endpoint, name='webhook_endpoint'),
    # path('api_voip/handle_incoming_call', views.handle_incoming_call),

    path('/voip/api_voip/call_status', views.twilio_call_status),

    path('make-calls/', views.make_calls, name='make_calls'),
    # path('twiml/', views.twiml, name='twiml'),  # Add this line to create a URL for the twiml view
    path("/voip/api_voip/handle_incoming_call", views.handle_incoming_call, name='get_all_solds'),
    path('send-message/', views.send_message_view, name='send_message'),


]