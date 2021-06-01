import pretty_errors
from datetime import date, datetime, timedelta
import re

#msg = "《旅程表》\n出發日期：2021/6/14\n結束日期：2021/06/16"
travel_plan_template = '''*住宿-
*早餐-
.09:00-
*午餐-
.14:00-
.16:00-
*晚餐-
—————
*備註：

'''


#判斷是否要執行「建立旅程表」指令
def if_set_travel_time(msg):
    result = re.match(r'^【建立旅程表】', msg)
    if result:
        return True
    else:
        return False

#輸入「建立旅程表」資訊，解析日期，輸出「旅程表」或是錯誤資訊
def set_travel_time(msg):
    #1. 抓出日期資訊字串
    try:
        travel_date = re.findall('\d+\W\d+\W\d+', msg)
        begin_date = travel_date[0]
        end_date = travel_date[1]
    except:
        return "想要新增旅行表，格式請參考以下範例：\n\n【建立旅程表】\n出發日期：2021/6/14\n結束日期：2021/6/18"
    
    #2. 解析日期datetime
    dateFormattor = "%Y/%m/%d" #日期解析格式
    begin_date = datetime.strptime(begin_date, dateFormattor)
    end_date = datetime.strptime(end_date, dateFormattor)

    #3. 判斷日期是否合法，如果不合法就列出提示訊息
    now_date = datetime.now()#抓出現在的時間datetime
    if_legal = True
    error_message = ""
    travel_plan = "《旅程表》\n"
    if begin_date > end_date: #如果 結束日期 早於 開始日期
        if_legal = False
        error_message += "-開始日期不能早於結束日期。\n"
    if (end_date - begin_date).days > 6:
        if_legal = False
        error_message += "-無法安排超過7天的行程。\n"
    if begin_date < now_date: #如果 開始日期 早於 今天
        if_legal = False
        error_message += "-開始日期不能早於今天。\n"
    if (end_date - now_date).days >= 365: #如果 結束日期 與 今天 相差超過365天
        if_legal = False
        error_message += "-無法安排超過一年後的行程。\n"

    #4.如果合法，則進一步製作旅程表；如果不合法，則輸出錯誤訊息
    if if_legal:
        all_date = [] #儲存所有日期的字典（未來可以作為儲存資料）
        append_date = begin_date
        while append_date <= end_date:
            all_date.append(append_date)
            append_date += timedelta(days=1)
        i = 1
        
        for date in all_date:
            str_date = datetime.strftime(date, '%m/%d')
            travel_plan += f'———————————\nDay{i}  {str_date}\n———————————\n{travel_plan_template}'
            i += 1
        return travel_plan
    else:
        return error_message
        
#def make_travel_plan():





reply_demo_list = {
    '自我介紹' : 
'''嗨！我是旅友，讓你的旅程更輕鬆。
- 你可以隨時輸入“旅友”來看看旅程的狀態。
- 如果有新的旅行計劃，你可以輸入“建立旅程表”來紀錄你的旅程構想。
- 如果想看看目前的旅行計劃，輸入“查看旅程表”，隨時可以更新計畫。''',
    '旅友':
'''嗨～想查看旅行計劃可以輸入“查看旅程表”，想規劃一個全新的旅行計畫可以輸入“建立旅程表”。''',
    '建立旅程表':
'''【建立旅程表】
出發日期：
結束日期：'''} 