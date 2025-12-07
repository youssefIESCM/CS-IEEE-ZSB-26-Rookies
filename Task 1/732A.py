k, r = map(int, input().split())
n = 1   
while True:
    prices = n * k
    last_digit = prices % 10
    if last_digit == 0 or last_digit == r:
        print(n)
        break
    n += 1