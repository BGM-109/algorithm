import itertools

m, n = map(int, input().split())

arr = list(map(int, input().split()))

result = list(itertools.combinations((arr), 3))

answer = [sum(x) for x in result if n - sum(x) >= 0]
answer.sort()
print(answer[-1])
