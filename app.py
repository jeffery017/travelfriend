from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
#import reply
#======這裡是呼叫的檔案內容=====
from module.reply import *
#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('KoMh6mioEL4546mZOPN9tQwLAVsBd+hO1EE17HshTEX8NjDCFNYZzm5gUE/DdVFHHBOAX/AQ6jtrmFbtn77nKHQm4OlX4E9jzj/QWDKlKjxoajsqQ+eJRh+AdnCRj5uTpQ13FvH8pBFnDgRYmGxamwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('7878e542df473710f6a5ab7c125b0007')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

reply_message = {"小雞":"嗶嗶","小狗":"汪汪","母牛":"哞哞","母雞":"咯咯","柯文哲":"你知道吼",}
travel_plan_example = "行程名稱\n--------\n出發地點：\n目的地：\n出發時間：\n回程時間：\n交通方式："
readme = "我是你的旅友，讓你的旅程更輕鬆。\n\n你可以輸入「新行程」，我會記起來你的旅行，在出發前替你記得要準備的東西。\n\n你也可以輸入「說明」，隨時查看我的規則。"
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if msg in reply_message:
        reply_msg = reply_message[msg]
    elif msg in reply_demo_list:
        reply_msg = reply_demo_list[msg]
    elif if_set_travel_time(msg):
        reply_msg = set_travel_time(msg)
    else:
        reply_msg = msg + '\n' + msg
    message = TextSendMessage(text=reply_msg)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
