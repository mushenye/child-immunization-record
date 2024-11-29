from django.core.mail import send_mail
from django.utils import timezone
from child_immunization import settings
from .models import ImmunizationSchedule
from twilio.rest import Client

def send_immunization_alerts():
    today = timezone.now().date()
    schedules = ImmunizationSchedule.objects.filter(due_date__lte=today, alert_sent=False)

    for schedule in schedules:
        child = schedule.child
        vaccine = schedule.vaccine
        message=f"The vaccine {vaccine.name} is due for {child.fullname}."
        # Send an email alert to the parent

  
    if child.parent.email_address:

        send_mail(
            subject=f"Immunization Alert for {child.fullname}",
            message=message,
            from_email="noreply@immunizationalerts.com",
            recipient_list=[child.parent.email_address],
        )

    send_sms_alert(child.parent.parent_phone_number, message)
    
    # Mark alert as sent
    schedule.alert_sent = True
    schedule.save()




def send_sms_alert(phone_number, message):
    # Initialize Twilio client with credentials
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    # Send SMS
    message = client.messages.create(
        body=message,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number
    )
    return message.sid  # Return message ID for confirmation



