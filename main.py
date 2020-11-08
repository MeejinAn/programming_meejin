from datetime import datetime, timedelta, date

while True:
    name = input("과제 이름을 입력해주세요. -> ")
    date1 = input("과제 기한을 입력해주세요. (ex. yyyy.mm.dd) -> ")
    y, m, d = date1.split(".")
    y = int(y)
    m = int(m)
    d = int(d)
    date2 = date(y, m, d)
    tday = date.today()

    if (date2 - tday).days < 0:
        print ("이미 지났습니다.")
        continue
    elif (date2 - tday).days == 0:
        print (name, "D-DAY")
        break
    else:
        print (name, "D-",(date2 - tday).days)
        break



