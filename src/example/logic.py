import math

q = int(input())
while q > 0:
    x = int(input())
    sum_of_series = (x * (x + 1)) // 2
    print((int(math.pow(sum_of_series, 9))) % 1000000007)
    q -= 1
