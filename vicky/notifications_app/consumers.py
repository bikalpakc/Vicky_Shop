from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

class NotificationsConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("Received connection req")
        await self.channel_layer.group_add('notifications', self.channel_name)
        await self.accept()
        print("Connection Accepted")

    async def disconnect(self):
        await self.channel_layer.group_discard('notifications', self.channel_name)

    async def send_notifications(self, event):
        message=json.loads(event['text'])

        await self.send(text_data=json.dumps(message))