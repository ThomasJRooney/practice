# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    nums = input()
    nums = nums.split(" ")
    rows = int(nums[0])
    cols = int(nums[1])
    block = ".|."
    top = ""
    bottom = ""
    for i in range(rows//2):
        row = block.center(cols, "-")
        if i != 0:
            top += "\n" + row
        else:
            top += row
        bottom = row + "\n" + bottom
        block += ".|..|."
    
    print(top)
    print("WELCOME".center(cols, "-"))
    print(bottom)