n= int(input())
q= input().lower()
unique= set(q)
alphabet= set(char for char in unique if char.isalpha())
if len(alphabet) == 26:
    print("YES")
else:
    print("NO")