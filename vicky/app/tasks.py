from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

#HTML Email required stuff
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@shared_task(bind=True)
def send_mail_func(self, user, ordered_items):
    # Send Normal Mail
    # mail_subject="Purchase Completed"
    # message="Thank you for shopping with us. The payment for your order has been recieved successfully. Order detail is as follows:<br> T-shirt1: Rs2000"
    
    # ------Or, write dynamic message as below:-----
    # item_details = "\n".join(
    #     [f"Product: {item.product.name}, Quantity: {item.quantity}" for item in ordered_items]
    # )
    # message = f"Dear {user.username},\n\nYour order has been placed successfully. Here are the details:\n\n{item_details}"

    # to_email=user.email
    # send_mail(
    #     subject=mail_subject,
    #     message=message,
    #     from_email=settings.EMAIL_HOST_USER,
    #     recipient_list=[to_email],
    #     fail_silently=True,
    # )
    # return("E-mail sent successfully")

    #Send the HTML Mail
    ordered_items=ordered_items
    to_email=user.email
    mail_subject="Purchase Completed"
    html_content=render_to_string("app/purchase_complete_email.html", {'ordered_items': ordered_items})
    text_content=strip_tags(html_content)

    email=EmailMultiAlternatives(
        # subject
        mail_subject,
        # content
        text_content,
        # from_email
        settings.EMAIL_HOST_USER,
        # recipient_list
        [to_email],
    )
    email.attach_alternative(html_content, "text/html")
    email.send()