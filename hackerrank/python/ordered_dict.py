from collections import OrderedDict
dic = OrderedDict()
items = int(input())
for item in range(items):
    inp = input().split()
    key = ""
    val = 0
    for x in inp:
        if x.isdigit():
            val = int(x)
        else:
            if key != "":
                key += " "
            key += x
    if key in dic:
        dic[key] += val
    else:
        dic[key] = val
for key, val in dic.items():
    print(key + " " + str(val))