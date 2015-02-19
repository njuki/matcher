from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http.response import HttpResponseForbidden
from django.shortcuts import render
import json
from smslogger.models import LoggedMessage
from smslogger.utils import get_pending

@csrf_exempt
def incomingsms(request):
    if request.method == 'POST':
        #get the phone number that sent the SMS.
        if "from" in request.POST and request.POST["from"]:
            sender = request.POST["from"]
        if "message" in request.POST and request.POST["message"]:
            message = request.POST["message"]

        if len(sender) > 0 and len(message) > 0:
            #if action == 'incoming':
            'LOG SMS INTO INCOMING SMS DATABASES'
            logged = LoggedMessage()
            logged.direction = LoggedMessage.DIRECTION_INCOMING
            logged.text = message
            logged.identity = sender
            logged.status = LoggedMessage.STATUS_INFO
            logged.save()
            success = "true"
        else:
            success = "false"

        reply = {"payload":{"success": success}}
        return HttpResponse(json.dumps(reply), content_type='application/json')
    if request.method == 'GET':

        data  = request.GET
        if request.GET.get('task'):
            action = request.GET['task']
            if action == 'send':
                #Querry SMS to send
                p = get_pending()
                if p:
                    payload = { "payload": {
                        "task": "send",
                        "messages": serialized_sms(p)}}
                    return HttpResponse(json.dumps(payload), content_type='application/json')
                else:
                    pass


def serialized_sms(p):
    y = []
    for x in p:
        z = {"to": x.identity, "message": x.text}
        y.append(z)
        x.status = LoggedMessage.STATUS_SUCCESS
        x.save()
    return y
