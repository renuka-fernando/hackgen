q = int(input())

for i in range(q):
    h1, m1, h2, m2 = map(int, input().split())
    k = int(input())
    delay = (h1 + k - h2) * 60 + m1 - m2
    print(delay)