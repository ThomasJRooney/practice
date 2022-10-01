from itertools import permutations
if __name__ == '__main__':
    i = input()
    i = i.split(" ")
    word = i[0]
    num = int(i[1])
    perms = list(permutations(word, num))
    perms.sort()
    out = ""
    for perm in perms:
        for i in range(len(perm)):
            out += perm[i]
        out += "\n"
    print(out)
