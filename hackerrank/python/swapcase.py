def swap_case(s):
    s = s.split(' ')
    out = ''
    for st in s:
        out += swap(st)
        out += ' '
    return out

def swap(s):
    for i in range(len(s)):
        if s[i].isupper():
            s = s[:i] + s[i].lower() + s[i+1:]
        elif s[i].islower():
            s = s[:i] + s[i].upper() + s[i+1:]
    return(''.join(s))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
