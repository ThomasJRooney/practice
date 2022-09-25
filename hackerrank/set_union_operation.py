# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    english = int(input())
    e_space = input()
    e_space = e_space.split(" ")
    french = int(input())
    f_space = input()
    f_space = f_space.split(" ")
    union = set()
    for space in e_space:
        union.add(space)
    for space in f_space:
        union.add(space)
    print(len(union))
    
