# Generated by Django 4.1.12 on 2023-11-06 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_calllogs_phone_rename_phone_no_contact_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]