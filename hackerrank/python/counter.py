from collections import Counter

shoes = int(input())
sizes = list(map(int, input().split()))
s_count = Counter(sizes)
money = 0
customers = int(input())
for i in range(customers):
    size_price = list(map(int, input().split()))
    size = size_price[0]
    price = size_price[1]
    if size in s_count:
        if s_count[size] > 0:
            s_count[size] -= 1
            money += price
print(money)