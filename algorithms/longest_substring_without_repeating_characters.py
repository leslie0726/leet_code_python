class Solution:
    def __init__(self):
        pass

    def lengthOfLongestSubstring(self, s: str) -> int:
        word_dict = {}
        length = 0
        max_length = 0
        check_point = 0
        for index in range(len(s)):
            # 有重複值以及大於等於之前檢查點，就更新長度跟檢查點
            if s[index] in word_dict.keys() and word_dict[s[index]] >= check_point:
                repeat_point = word_dict[s[index]]
                length = (index + 1) - (repeat_point + 1)
                check_point = repeat_point
            # 檢查後，沒重複
            else:
                length += 1
            word_dict[s[index]] = index
            max_length = max(max_length, length)
        return max_length
