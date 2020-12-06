from datetime import datetime, timedelta, date

def print_help():
    print ("0 : 현재 날짜 기준으로 D-DAY 계산하기")
    print ("1 : 특정 일자 기준으로 D-DAY 계산하기")
    print ("2 : 프로그램 종료")
while True:
    print_help()
    choice = input("번호를 선택해주세요 -> ")
    if choice == "0":
        while True:
            name1 = input("과제 이름을 입력해주세요. -> ")
            deadline1 = input("과제 기한을 입력해주세요. ex) yyyy.mm.dd -> ")
            y, m, d = deadline1.split(".")
            y = int(y)
            m = int(m)
            d = int(d)
            deadline2 = date(y, m, d)
            Today = date.today()
            if (deadline2 - Today).days < 0:
                print ("이미 지났습니다. 다시 입력해주세요.")
                continue
            elif (deadline2 - Today).days == 0:
                print (name1, " : D-DAY")
                break
            else:
                print (name1, " : D-", (deadline2 - Today).days)
                break
    elif choice == "1":
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
                print ("이미 지났습니다")
                continue
            elif (deadline_2 - date_2).days == 0:
                print (name_1, "D-DAY")
                break
            else:
                print (name_1, "D-", (deadline_2 - date_2).days)
                break
    elif choice == "2":
        break
    else:
        print ("잘못 선택하셨습니다. 번호를 다시 입력해주세요")