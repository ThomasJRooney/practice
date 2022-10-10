n = int(input())
for i in range(n):
    s = input()
    vowel = "aeiou"
    happy = False
    for i in range(len(s) - 2):
        count = 0
        for c in s[i:i+3]:
            if c in vowel:
                count += 1
        if count == 3:
            happy = True

    print("Happy" if happy else "Sad")
