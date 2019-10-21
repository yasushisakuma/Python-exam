print("5つの入力をしてください.")
list1 = [input() for i in range(5)]
print("入力の2番目に4を追加します.")
list1.insert(1,"4")
print(list1)