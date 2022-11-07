class Solution:
    def maximum69Number (self, num: int) -> int:
        test = str(num)
        for i in range(len(test)):
            if test[i] == '6':
                test = test[:i] + '9' + test[i + 1:]
                break
        return int(test)
