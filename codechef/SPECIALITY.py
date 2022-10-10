n = int(input())
for i in range(n):
    ste = list(map(int, input().split()))
    if ste[0] > ste[1] and ste[0] > ste[2]:
        print("Setter")
    elif ste[1] > ste[0] and ste[1] > ste[2]:
        print("Tester")
    elif ste[2] > ste[1] and ste[2] > ste[0]:
        print("Editorialist")