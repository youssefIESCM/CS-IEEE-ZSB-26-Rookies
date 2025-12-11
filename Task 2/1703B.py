letters = int(input())

for _ in range(letters):
    number = int(input())
    characters = input().strip()

    solved = set()
    balloons = 0

    for ch in characters:
        if ch not in solved:
            balloons += 2
            solved.add(ch)
        else:
            balloons += 1

    print(balloons)
