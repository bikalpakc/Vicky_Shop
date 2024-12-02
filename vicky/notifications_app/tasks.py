from tokenize import Ignore
import requests
import asyncio
from celery import shared_task
from .models import Notification
import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
channel_layer=get_channel_layer() #gets and sets default channel layer described in settings.py file.

@shared_task(bind=True) #to let know Celery that this is a task to be executed.
def get_notification(self, data):
    print(data)
    try:
        notification=Notification.objects.filter(id=int(data))
        if notification.exists():  # Use exists() to check if a queryset contains results
            notification=notification.first()
            channel_layer=get_channel_layer()

            # #This method gives error in Celery so we will use the another (uncommented) method.
            # async_to_sync(channel_layer.group_send)('notifications', {'type':'send_notifications', 'text':notification}) #Send message to the Django Channels group and 'type' is the method that handles the send method. For e.g. if type is send_notifications, it is handled by method send_notifications in consumers.py file. whereas, 'text' is equivalent to 'context' in views.py of http request.

            loop=asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(
                channel_layer.group_send(
                    'notifications', 
                    {'type': 'send_notifications', 'text': json.dumps(notification.message)}
                )
            )

            notification.sent=True
            notification.save()
            return 'Done'
        
        else:
            self.update_state(
                state='FAILURE',
                meta={'exe': 'Not Found'}
            )
            
            raise Ignore()

    except:
        self.update_state(
                state='FAILURE',
                meta={'exe': 'FAILED'}
            )
            
        raise Ignore()    