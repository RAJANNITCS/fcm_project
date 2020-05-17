from django.http import HttpResponse
from django.shortcuts import render
from pyfcm import FCMNotification
from rest_framework.response import Response
from rest_framework import status
from myapp.models import Token
# Create your views here.
from django.views import View


def index(request):
    return render(request, 'index.html')


class ServiceWorkerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'firebase-messaging-sw.js', content_type="application/x-javascript")


class WebPush:
    def single_device(self):
        tokens = Token.objects.all()
        tokens = tokens.last()
        push_service = FCMNotification(
        api_key="AAAAdNdLJO0:APA91bEQzRO44Q5ezSXC8xp-G5nC5DGkRo_ghbxhHTvQvwUnSNg7qIkqBNRYDuaB6EicVUCcBf4LRIZHAzWqUpGOrd9A9Y3b9Y7_EP0TBPw_wbOJr7RxztI2uakcEIUwdmmk_qITHdVl")
        registration_id = tokens.token
        message_title = "Push Notifications"
        message_body = "Hi users "
        result = push_service.notify_single_device(
        registration_id=registration_id, message_title=message_title, message_body=message_body)
        return HttpResponse(push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body))

    def multiple_device(self):
        tokens = Token.objects.all().values_list('token', flat=True)
        tokens = list(tokens)
        push_service = FCMNotification(
        api_key="AAAAdNdLJO0:APA91bEQzRO44Q5ezSXC8xp-G5nC5DGkRo_ghbxhHTvQvwUnSNg7qIkqBNRYDuaB6EicVUCcBf4LRIZHAzWqUpGOrd9A9Y3b9Y7_EP0TBPw_wbOJr7RxztI2uakcEIUwdmmk_qITHdVl")
        registration_ids = tokens
        message_title = "multiple device"
        message_body = "Hi user "
        result = push_service.notify_multiple_devices(
        registration_ids=registration_ids, message_title=message_title, message_body=message_body)
        return HttpResponse(push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body))
