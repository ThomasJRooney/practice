n = int(input())
for i in range(n):
    try:
        ab = list(map(int, input().split()))
        try:
            print(ab[0] // ab[1])
        except ZeroDivisionError as e:
            print("Error Code:", e)
    except ValueError as ve:
        print("Error Code:", ve)