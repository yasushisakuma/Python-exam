print("5つの入力をしてください.")
list1=[input() for i in range(5)]

newlist = list(reversed(list1))
print("入力を逆順に表示します.")
print(newlist)