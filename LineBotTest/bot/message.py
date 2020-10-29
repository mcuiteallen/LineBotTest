# import 必要的函式庫
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import json
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
to = "Ua86721edba45ff594fe7ed49689de624"  ##mcuiteallen
# to = "C2e069a7b87e247b0a11458dddaa2b4f5"

@csrf_exempt
def push(request):
    try:
        body = request.body.decode('utf-8')
        data = json.loads(body)
        print('data[message]=', data['messages'][0]['text'])
        line_bot_api.push_message(to, TextSendMessage(text=data['messages'][0]['text']))
    except LineBotApiError as e:
        raise e

