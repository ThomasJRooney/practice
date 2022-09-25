def do_command(l, command):
    command = command.split(" ")
    op = command[0]
    if op == 'insert':
        l.insert(int(command[1]), int(command[2]))
    elif op == 'print':
        print(l)
    elif op == 'remove':
        l.remove(int(command[1]))
    elif op == 'append':
        l.append(int(command[1]))
    elif op == 'sort':
        l.sort()
    elif op == 'pop':
        l.pop()
    elif op == 'reverse':
        l.reverse()
    return l

if __name__ == '__main__':
    N = int(input())
    commands = []
    for n in range(N):
        commands.append(input())
    l = []
    for c in commands:
        l = do_command(l, c)
