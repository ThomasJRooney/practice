from itertools import product
if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = list(product(a, b))
    out = ""
    for s in ab:
        out += str(s)
        out += " "
    print(out)
