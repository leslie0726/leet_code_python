from algorithms.length_of_last_word import Solution


def test_length_of_last_word_success():
    obj = Solution()
    assert obj.lengthOfLastWord('Hello World') == 5
    assert obj.lengthOfLastWord('   fly me   to   the moon  ') == 4
    assert obj.lengthOfLastWord('luffy is still joyboy') == 6
