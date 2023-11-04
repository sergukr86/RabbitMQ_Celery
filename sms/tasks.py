import os

from django.conf import settings

from celery import shared_task

from twilio.rest import Client


client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


@shared_task
def send_sms(receiver, message):
    send_message = client.messages.create(body=message, from_="+13345181530", to=receiver)
    return send_message.sid
