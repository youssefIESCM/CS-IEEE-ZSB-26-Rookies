words = input()
all_upper = words.isupper()
all_but_first_isupper = len(words) == 1 or (words[0].islower() and words[1:].isupper())
if all_upper or all_but_first_isupper: 
    print(words.swapcase())
else:
    print(words)