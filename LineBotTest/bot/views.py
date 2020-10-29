# import 必要的函式庫
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json
import ssl
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
# 這邊是Linebot的授權TOKEN(等等註冊LineDeveloper帳號會取得)，我們為DEMO方便暫時存在settings裡面存取，實際上使用的時候記得設成環境變數，不要公開在程式碼裡喔！
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
#from django.conf import json
ssl._create_default_https_context = ssl._create_unverified_context


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        print('body=', body)
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                main(event)
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

def getPackageUrl(url):
    contents = urllib.request.urlopen(url).read()
    body = json.loads(contents)
    #print('contents=', contents)
    return body['Result']  

def main(event):
    repley_text = event.message.text
    reply_token = event.reply_token
    if "下單"  in repley_text:
        #data={}
        #tmpSource={}
        #event={"message": {"id": "12596308547918", "text": "2222", "type": "text"}, "replyToken": "8ffd829f84804171aec87a9faaafae26", "source": {"roomId": "R7cae8b1965a792f95594a3b824448782", "type": "room", "userId": "Ua86721edba45ff594fe7ed49689de624"}, "timestamp": 1598864954261, "type": "message"}
        #tmpSource["roomId"]=event.source.room_id
        #tmpSource["userId"]=event.source.user_id
        #data["replyToken"]=reply_token
        #data["source"]=tmpSource
        #url="https://xxx.ak-platform.com:8443/order/signOn"
        #headers = {'Accept': '*/*', 'Content-Type': 'application/json'}
        #params = json.dumps(data).encode('utf8')
        #contents = urllib.request.Request(url, headers=headers, data=params)
        #response = urllib.request.urlopen(contents).read()
        #sendMessage(reply_token, str("不理你"))
        #sendMessage(reply_token, "歡迎" + name + "!! \n 請透過此連結下單\nhttps://xxx.ak-platform.com:8443/?id=" + event.source.room_id + event.source.user_id + "&password=" + reply_token)
        sendMessage(reply_token, "歡迎!! \n 請透過此連結下單\nhttps://gogo911.net/")
        #packageUrl = str(getPackageUrl()).strip("b'")

    elif "2222"  in repley_text:
        sendMessage(reply_token, str(event))
    elif "寶貝"  in repley_text:
        sendMessage(reply_token, str("是老大!!!"))        
    elif  repley_text == "公告":
        res = getPackageUrl('https://xxx.ak-platform.com:8443/order/getAnnouncement')
        #sendMessage(reply_token, str("（（重要公告））9/2【539】臨時擋牌通知：（20x21x33x其他）二星中4千6，46碰（含）以上獎金正常。（05x08x11x20x21x30x33x其他）三星中3萬5，166碰（含）以上獎金正常，四星中25萬，331碰（含）以上獎金正常。"))       
        sendMessage(reply_token, str(res)) 
    elif  repley_text == "功能":
        sendMessage(reply_token, "目前有三個功能!! \n 1 公告\n 2 下單")      
    #elif repley_text == "全部公告":
        #res = getPackageUrl('https://xxx.ak-platform.com:8443/order/getAllAnnouncement')
        #sendMessage(reply_token, str("((重要公告))9/2【539】臨時擋牌通知：（20x21x33x其他）二星中4千6，46碰（含）以上獎金正常。（05x08x11x20x21x30x33x其他）三星中3萬5，166碰（含）以上獎金正常，四星中25萬，331碰（含）以上獎金正常。,4376,2020-09-02 18:46:58,5,N,0000-00-00 00:00:00|1,\\n((重要公告))9/2【539】擋牌通知：（04x05x08x09x25x30）二星中4千，46碰（含）以上獎金正常。（05x09x30x其他）二星中4千6，46碰（含）以上獎金正常。（04x05x08x09x11x22x25x30x33x38x其他）三星中4萬8，166碰（含）以上獎金正常，四星中55萬，331碰（含）以上獎金正常。下注完畢顯示下注成功視窗後，請各會員一定要至下注明細查看注單，若有顯示固定賠時務必要點進去查看是否有降賠，賠率以固定賠為準，若多組同時開出降倍，中獎金額依最低組數及賠率為主。            ,4374,2020-09-02 16:37:33,5,N,0000-00-00 00:00:00|1,\\n((重要公告))9/1【539】臨時擋牌通知：（09x23x25x其他）二星中4千6，46碰（含）以上獎金正常。（05x09x11x23x25x33x37x其他）三星中3萬5，166碰（含）以上獎金正常，四星中25萬，331碰（含）以上獎金正常。,4372,2020-09-01 18:47:16,5,N,0000-00-00 00:00:00|1,\\n((重要公告))9/1【539】擋牌通知：（04x05x08x23x25x30）二星中4千，46碰（含）以上獎金正常。（05x22x30x其他）二星中4千6，46碰（含）以上獎金正常。（04x05x08x09x15x22x23x25x30x38x其他）三星中4萬8，166碰（含）以上獎金正常，四星中55萬，331碰（含）以上獎金正常。下注完畢顯示下注成功視窗後，請各會員一定要至下注明細查看注單，若有顯示固定賠時務必要點進去查看是否有降賠，賠率以固定賠為準，若多組同時開出降倍，中獎金額依最低組數及賠率為主。           ,4370,2020-09-01 16:36:28,5,N,0000-00-00 00:00:00|1,\\n((重要公告))5/4起，539四星賠率改為7500倍，1000碰（含）以上為8000倍，如有異動另行通知，謝謝 ！,4004,2020-05-22 16:44:46,5,N,2020-05-25 16:49:13|1,\\n((重要公告))3/12 起【加州彩】已全面調降價格， 請各位會員踴躍下注。,3818,2020-03-12 18:31:49,5,N,0000-00-00 00:00:00|1,\\n((重要公告))【加州彩】3月9日星期一開始配合美國夏令時間，關盤時間更改為早上 9：20 請各位會員多加注意！,3790,2020-03-05 20:47:29,5,N,0000-00-00 00:00:00|1,\\n((重要公告))本公司一律不收以下牌型，如：兩星組數為１號ｘ全部、三星組數為１號ｘ１號ｘ全部、四星組數為１號ｘ１號ｘ１號ｘ全部，及其它拆牌組，本公司有權自行刪單，不另行通知 。,2249,2018-12-21 17:35:20,5,N,0000-00-00 00:00:00|1,（重要公告）下注後15分鐘後不能刪單，請審慎下單，造成不便敬請見諒！！,14,2016-09-13 17:34:03,5,N,2017-06-01 16:33:26|1,（重要公告）請會員一定要至下注明細查看注單並確認注單是否正確，若有顯示固定賠或特殊牌型時務必要點進去查看是否有降賠，如號碼遇到漲價或降倍應自行承擔不得異議。開獎後如有任何爭議，以派彩後注單為依據，盤中臨時漲價或降倍不另行通知，請會員謹慎下注。,8,2016-09-11 00:26:27,5,N,2020-04-01 16:38:37\"}\\n"))               
        #sendMessage(reply_token, str(res))               
    #else:
    #    sendMessage(reply_token, "我可以做這些事\n1.最新版安裝包下載路徑\n2.wifi密碼\n3.cs網址\n請輸入編號代碼")

def sendMessage(reply_token, text):
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(text=text)
    )

