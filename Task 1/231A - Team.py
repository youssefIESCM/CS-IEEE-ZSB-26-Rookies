n = int(input())
count = 0

for _ in range(n):
    P, V, T = map(int, input().split())
    if P + V + T >= 2:
        count += 1

print(count)