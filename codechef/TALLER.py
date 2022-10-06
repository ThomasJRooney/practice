n = int(input())
for i in range(n):
    ab = list(map(int, input().split()))
    if ab[0] > ab[1]:
        print("A")
    else:
        print("B")
        
