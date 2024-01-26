class Solution:
    def __init__(self):
        pass

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        result = s[0:1]
        for center in range(1, len(s)):
            flag1 = True;
            flag2 = True;
            shift = 1
            while True:
                if not(center - shift >=0 and center + shift <= len(s)):
                    break;
                max = center + shift
                max2 = center + shift -1;
                min = center - shift

                if flag1 and isPalindromicSubstring(s, max, min):
                    result = updateMaxResult(s, min, max, result)
                else:
                    flag1 = False

                if flag2 and isPalindromicSubstring(s, max2, min):
                    result = updateMaxResult(s, min, max2, result)
                else:
                    flag2 = False
                if not flag1 and not flag2:
                    break
                shift += 1
        return result

def isPalindromicSubstring(s: str, max: int, min: int) -> bool:
    return max != len(s) and s[min] == s[max]

def isValidIndex(s: str, center: int, shift: int) -> bool:
    min = center - shift
    max = center + shift
    return min >= 0 and max <= len(s)

def updateMaxResult(s: str, min: int, max: int, result: str) -> str:
    find = s[min:(max+1)]
    if len(find) > len(result):
        result = find
    return result