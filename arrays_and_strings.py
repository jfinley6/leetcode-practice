from typing import List

class Solution:
    # Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.
    def findClosestNumber(self, nums: List[int]) -> int:
        closestNum = nums[0]

        for num in nums:
            if abs(num) < abs(closestNum):
                closestNum = num
        
        if closestNum < 0 and abs(closestNum) in nums:
            return abs(closestNum)
        else:
            return closestNum

    # You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_length, word2_length = len(word1), len(word2)
        word1_index, word2_index = 0, 0
        mergedList = []
        word = 1
        while word1_index < word1_length and word2_index < word2_length:
            if (word == 1):
                mergedList += word1[word1_index]
                word1_index += 1
                word = 2
            if (word == 2):
                mergedList += word2[word2_index]
                word2_index += 1
                word = 1

        while word1_index < word1_length:
            mergedList += word1[word1_index]
            word1_index += 1

        while word2_index < word2_length:
            mergedList += word2[word2_index]
            word2_index += 1

        return ' '.join(mergedList)
        
    
# Create an instance of the Solution class
solution = Solution()

# findClosestNumber cases
# # Output: 1
# print(solution.findClosestNumber([-4,-2,1,4,8]))
# # Output: 1
# print(solution.findClosestNumber([2,-1,1]))

# mergeAlternatively cases
# # Output: a p b q c r
# print(solution.mergeAlternately("abc", "pqr"))
# # Output: a p b q r s
# print(solution.mergeAlternately("ab", "pqrs"))
# # Output: a p b q c d
# print(solution.mergeAlternately("abcd", "pq"))