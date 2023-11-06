import os
from django.core.management.base import BaseCommand
from search.models import Contact

class Command(BaseCommand):
    help = 'Import address extra'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        csv_file_path = "C:/Users/shaik/Downloads/agent_leads (1).csv"  # Update the file path accordingly

        with open(csv_file_path, "r") as csvData:
            for lead in csvData.readlines():
                lead_data = lead.split(",")  # Assuming the data is comma-separated
                name = lead_data[0].strip()
                state = lead_data[1].strip()
                email = lead_data[2].strip()
                phone = lead_data[3].strip()
                sold_sands = lead_data[4].strip()

                # Don't allow duplicate phone numbers
                if Contact.objects.filter(phone=phone).first():
                    print(f"We already have imported this lead with phone number: {phone}")
                    continue

                
                contact = Contact()
                contact.name = name
                contact.state = state
                contact.email = email
                contact.phone = phone
                contact.sold_sands = sold_sands

                contact.save()
