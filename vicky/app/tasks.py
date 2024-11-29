from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
@shared_task(bind=True)
def send_mail_func(self, user):
    mail_subject="Purchase Completed"
    message="Thank you for shopping with us. The payment for your order has been recieved successfully. Order detail is as follows:<br> T-shirt1: Rs2000"
    to_email=user.email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )
    return("E-mail sent successfully")