def print_rangoli(size):
    if size == 1:
        print("a")
        return
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    idx = 0
    mid = ""
    block = alphabet[idx]
    width = (size - 1) * 4 + 1
    while idx < size - 1:
        idx += 1
        block = alphabet[idx] + "-" + block + "-" + alphabet[idx]
        mid = block
    mid += "\n"
    top = ""
    bottom = ""
    for i in range(size - 1):
        m = len(block) // 2
        if m < 3:
            block = block[0]
        else:
            block = block[:m - 3] + block[m+1:]
    
        top = block.center(width, "-") + "\n" + top
        bottom += block.center(width, "-") + "\n"
    
    print(top + mid + bottom)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)