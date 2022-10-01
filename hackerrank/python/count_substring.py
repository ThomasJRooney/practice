def count_substring(string, sub_string):
    lenSS = len(sub_string)
    idx = 0
    count = 0
    while idx + lenSS - 1 < len(string):
        if string[idx:idx + lenSS] == sub_string:
            count += 1
        idx += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
