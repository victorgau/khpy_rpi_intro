from settings import LINE_NOTIFY_TOKEN
from linenotify import Notify

# 欲傳送的訊息內容
message = '夭壽啊！溫濕度超級異常！'

Notify(LINE_NOTIFY_TOKEN, message)