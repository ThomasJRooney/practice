import textwrap

def wrap(string, max_width):
    string = list(string)
    lines = len(string) // max_width
    idx = 0
    st = ""
    for i in range(lines):
        for j in range(max_width):
            st += string[idx]
            idx += 1
        st += "\n"
    while idx < len(string):
        st += string[idx]
        idx += 1
    return(st)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
