i = int(input())
for q in range(i):
    n= int(input())
    scentence = input().split()
    s= scentence[0]
    t=scentence[1]
    if sorted(s)==sorted(t):
        print("yes")
    else:
        print("no")