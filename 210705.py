# 백준 벌집

# n = int(input())

# last = 1
# line = 1

# while True:
#     if n > last:
#         last += 6 * line
#         line += 1
#     else:
#         print(line)
#         break

# 손익분기점

# a, b, c = map(int, input().split())


# def solution(a, b, c):
#     if c == b:
#         return -1
#     n = a / (c - b)
#     if n < 0:
#         return -1
#     return int(n) + 1


# print(solution(a, b, c))

# 제로 - 스택

# n = int(input())

# arr = []
# for i in range(n):
#     m = int(input())
#     if m != 0:
#         arr.append(m)
#     else:
#         arr.pop()


# print(sum(arr))

# 백준 실버5 다리놓기 1010
import math

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)
