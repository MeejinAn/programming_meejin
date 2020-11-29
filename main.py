from datetime import datetime, timedelta, date

'''
while True:
    name = input("과제 이름을 입력해주세요. -> ")
    date1 = input("과제 기한을 입력해주세요. (ex. yyyy.mm.dd) -> ")
    y, m, d = date1.split(".")
    y = int(y)
    m = int(m)
    d = int(d)
    date2 = date(y, m, d)
    Today = date.today()

    if (date2 - Today).days < 0:
        print ("이미 지났습니다. 다시 입력해주세요.")
        continue
    elif (date2 - Today).days == 0:
        print (name, "D-DAY")
        break
    else:
        print (name, "D-",(date2 - Today).days)
        break
'''

while True:
    date_1 = input("기준 일자를 입력해주세요. ex) yyyy.mm.dd -> ")
    name_1 = input("과제 이름을 입력해주세요. -> ")
    deadline_1 = input("과제 기한을 입력해주세요. ex) yyyy.mm.dd -> ")
    y1, m1, d1 = date_1.split(".")
    y1 = int(y1)
    m1 = int(m1)
    d1 = int(d1)
    y2, m2, d2 = deadline_1.split(".")
    y2 = int(y2)
    m2 = int(m2)
    d2 = int(d2)
    date_2 = date(y1, m1, d1)
    deadline_2 = date(y2, m2, d2)
    if (deadline_2 - date_2).days < 0:
        print ("이미 지났습니다. 다시 입력해주세요")
        continue
    elif (deadline_2 - date_2).days == 0:
        print (name_1, "D-DAY")
        break
    else:
        print (name_1, "D-", (deadline_2 - date_2).days)
        break