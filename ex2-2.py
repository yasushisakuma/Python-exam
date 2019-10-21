import datetime
print("1つ目の日付を入力してください.")
year1 = input("年：")
month1 = input("月：")
day1 = input("日：")
dt1 = datetime.date(int(year1), int(month1), int(day1))
print("2つ目の日付を入力してください.")
year2 = input("年：")
month2 = input("月：")
day2 = input("日：")
dt2 = datetime.date(int(year2), int(month2), int(day2))

day = (dt1-dt2).days
print ("２つの日付間の日数は%d日です."%day)