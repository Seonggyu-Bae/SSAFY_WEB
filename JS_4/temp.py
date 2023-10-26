N = int(input())

num_list = list(map(int, input().split()))

ans = 0
for x in num_list:
    if x == 1:
        continue
    for i in range(2,x):
        if x % i ==0:
            break
    else:
        ans += 1

print(ans)