from algorithms.longest_palindromic_substring import Solution


def test_longest_palindromic_substring_success():
    obj = Solution()
    assert obj.longestPalindrome("babad") == "bab"
    assert obj.longestPalindrome("cbbd") == "bb"
    assert obj.longestPalindrome("a") == "a"
    assert obj.longestPalindrome("ac") == "a"
    assert obj.longestPalindrome("aacabdkacaa") == "aca"
    assert obj.longestPalindrome("bb") == "bb"
    assert obj.longestPalindrome("aaaa") == "aaaa"
    assert obj.longestPalindrome("ccc") == "ccc"
    assert obj.longestPalindrome("tattarrattat") == "tattarrattat"

