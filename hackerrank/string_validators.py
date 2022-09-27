if __name__ == '__main__':
    s = input()
    s = list(s)
    alnum = False
    al = False
    dig = False
    low = False
    up = False
    for c in s:
        if c.isalnum():
            alnum = True
        if c.isalpha():
            al = True
        if c.isdigit():
            dig = True
        if c.islower():
            low = True
        if c.isupper():
            up = True
    print(alnum)
    print(al)
    print(dig)
    print(low)
    print(up)
