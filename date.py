import datetime

now = datetime.datetime.now()

print("{}년 {}월 {}일".format(
    now.year,
    now.month,
    now.day
))

if now.hour < 12:
    print("오전 {}시 입니다.".format(now.hour))

if now.hour >= 12:
    print("오후 {}시 입니다.".format(now.hour))

    