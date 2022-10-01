if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        l = list(map(int, input().split()))
        if l[2] >= l[0] and l[2] < l[1]:
            print("yes")
        else:
            print("no")