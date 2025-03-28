from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 0;
        for index in range(len(digits)-1,-1,-1):
            if index == len(digits)-1:
                digits[index]+=1
            digits[index]+=plus
            plus = 0
            if digits[index]==10:
                digits[index]=0
                plus+=1
        result=[]
        if plus ==1:
            result.append(1)
        result[plus:plus + len(digits)] = digits
        return result