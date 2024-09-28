#leetcode solution to romanToInteger
class Solution(object):
    def romanToInt(self, s):
        romanNumbers = {
            'I' : 1,
            'V': 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        convertedSum = 0

        for i in range(len(s)):
            if i < len(s) - 1 and romanNumbers[s[i]] < romanNumbers[s[i + 1]]:
                convertedSum -= romanNumbers[s[i]]

            else:
                convertedSum += romanNumbers[s[i]]

        return convertedSum