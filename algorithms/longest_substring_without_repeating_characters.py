class Solution:
    def __init__(self):
        pass

    def lengthOfLongestSubstring(self, s: str) -> int:
        word_dict = {}
        count = 0
        result = 0
        check = 0
        for i in range(len(s)):
            if s[i] in word_dict.keys():
                if word_dict[s[i]] >= check:
                    count = (i+1) - (word_dict[s[i]]+1)
                else:
                    count+=1
                check = max(check, word_dict[s[i]])
            else:
                count += 1
            word_dict[s[i]] = i
            result = max(result, count)
        return result
