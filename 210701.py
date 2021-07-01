n = int(input())

arr = []

for i in range(n):
    l = list(map(int, input().split()))
    arr.append(l)

answer = [len([j for j in arr if i[0] < j[0] and i[1] < j[1]])+1 for i in arr]

for _ in answer:
    print(_, end=" ")


#   부르트포스 덩치
