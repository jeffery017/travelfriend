import pretty_errors
from datetime import datetime, timedelta

now_date = datetime.now()

dateFormattor = "%Y/%m/%d"
end_date = datetime.strptime('2021/10/15', dateFormattor)
begin_date = datetime(2021,8,1)

'''all_date = []
append_date = begin_date
while append_date <= end_date:
    all_date.append(append_date)
    append_date += timedelta(days=1)
for date in all_date:
    print(datetime.strftime(date,'%m/%d'))'''

all_date = {begin_date:"第一天", end_date:"最後一天"}
print(all_date)
'''
datetime.strptime() #parser解析，字串轉datetime
datetime.strftime() #format格式，datetime轉字串
'''