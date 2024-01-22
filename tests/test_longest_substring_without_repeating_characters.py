from algorithms.longest_substring_without_repeating_characters import Solution



def test_length_of_longest_substring_success():
    obj = Solution()
    assert obj.lengthOfLongestSubstring("abcabcbb") == 3
    assert obj.lengthOfLongestSubstring("bbbbb") == 1
    assert obj.lengthOfLongestSubstring("pwwkew") == 3
    assert obj.lengthOfLongestSubstring("dvdf") == 3
    assert obj.lengthOfLongestSubstring("abba") == 2
    assert obj.lengthOfLongestSubstring("tmmzuxt") == 5



