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
    path('make-calls/', views.make_calls, name='make_calls'),
    # path('twiml/', views.twiml, name='twiml'),  # Add this line to create a URL for the twiml view

]