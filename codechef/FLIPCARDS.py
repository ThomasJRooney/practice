n = int(input())
for i in range(n):
    cards = list(map(int, input().split()))
    faceup = cards[1]
    cards = cards[0]

    print(min(abs(cards - faceup), faceup))
