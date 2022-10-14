def minion_game(string):
    l, kevin, stuart = len(string), 0, 0
    for i in range(l):
        if string[i] in "AEIOU":
            kevin += l - i    
    if l % 2 == 0:    
        stuart = ((l+1)*l//2) - kevin
    else:
        stuart = ((l+1)*(l//2)+((l+1)/2)) - kevin  
    if stuart > kevin:
        print("Stuart {}".format(stuart))
    elif stuart < kevin:
        print("Kevin {}".format(kevin))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)