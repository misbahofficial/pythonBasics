"""
Sum of consecutive numbers.

Heads Up: Copying without credit is restricted.

"""

N = int(input())
sum = 0

for i in range(1, N+1):
    sum += i
print(sum)