import re
n = int(input())
for i in range(n):
    try:
        re.compile(input())
        print("True")
    except re.error:
        print("False")