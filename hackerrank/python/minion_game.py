def minion_game(string):
    stuart, kevin = 0, 0
    vowels = "aeiouAEIOU"
    subs = [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
    for ss in subs:
        if ss[0] in vowels:
            kevin += 1
        else:
            stuart += 1
    print("Stuart " + str(stuart) if stuart > kevin else "Kevin " + str(kevin))

if __name__ == '__main__':
    s = input()
    minion_game(s)