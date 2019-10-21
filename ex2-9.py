print("正の整数(7まで)の逆数の和を計算します.")

num = int(1)
ans = int(0)
for i in range(7):
    ans += 1/num
    num += 1

print(ans)