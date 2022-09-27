'''
Given an integer, convert it to a roman numeral.
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        conversion = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M", 4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
        roman = ""
        place = len(str(num)) - 1
        for n in str(num):
            n = int(n)
            goal = n *(10**(place))
            if goal in conversion:
                roman += conversion[goal]
            else:
                if n >= 5:
                    goal = 5 * (10**place)
                    roman += conversion[goal]
                    n -= 5
                if n > 0:
                    goal = n *(10**(place))
                    goal /= n
                    for i in range(n):
                        roman += conversion[goal]
            place -= 1 
        return roman
            
            
            
            
            
            
            
