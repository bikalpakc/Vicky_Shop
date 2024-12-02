from django.db import models
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django.db.models.signals import post_save
import json
# Create your models here.

class Notification(models.Model):
    message=models.TextField()
    send_on=models.DateTimeField()
    sent=models.BooleanField(default=False)

    class Meta:
        ordering=['-send_on']

@receiver(post_save, sender=Notification) 
def notification_handler(sender, instance, created, **kwargs):
    if created:
        print("Model created")
        schedule, created=CrontabSchedule.objects.get_or_create(hour=instance.send_on.hour, minute=instance.send_on.minute, day_of_month=instance.send_on.day, month_of_year=instance.send_on.month)
        print("1st line executed")
        task=PeriodicTask.objects.create(crontab=schedule, name='send-notification-'+str(instance.id), task="notifications_app.tasks.get_notification", args=json.dumps([instance.id]))       
        print("Second line executed")