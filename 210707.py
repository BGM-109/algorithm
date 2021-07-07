# 분해합 부르트포스

n = int(input())

arr = []


def fun(x):
    return x + sum([int(i) for i in str(x)])


for i in range(1, n+1):
    if fun(i) == n:
        arr.append(i)

ans = min(arr) if arr != [] else 0

print(ans)
