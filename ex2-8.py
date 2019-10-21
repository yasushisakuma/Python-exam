import math
print("2点間の距離を求めます.")
x1 = input("x1：")
x1 = float(x1)
y1 = input("y1：")
y1 = float(y1)
x2 = input("x2：")
x2 = float(x2)
y2 = input("y2：")
y2 = float(y2)

dis = math.sqrt((x2-x1)**2+(y2-y1)**2)
print("2点間の距離は%fです."%dis)