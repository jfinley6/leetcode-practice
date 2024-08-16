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

    # Given a roman numeral, convert it to an integer.
    def romanToInt(self, s: str) -> str:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        sum = 0
        n = len(s)
        i = 0
        while i < n:
            if i < n - 1 and d[s[i]] < d[s[i+1]]:
                sum += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                sum += d[s[i]]
                i += 1

        return sum

    # Given two strings s and t, return true if s is a subsequence of t, or false otherwise. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        s_len, t_len = len(s), len(t)

        if s == '': return True
        if s_len > t_len: return False

        for j in range(t_len):
            if t[j] == s[i]:
                if i == s_len - 1:
                    return True
                i += 1

        return False

    # You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit
    
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

# romanToInt cases
# Output: 3
# print(solution.romanToInt("III"))
# Output: 58
# print(solution.romanToInt("LVIII"))
# Output: 1994
# print(solution.romanToInt("MCMXCIV"))

# isSubsequence cases
# Output: true
# print(solution.isSubsequence("abc", "ahbgdc"))
# Output: false
# print(solution.isSubsequence("axc", "ahbgdc"))

# maxProfit cases
# Output: 5
print(solution.maxProfit([7,1,5,3,6,4]))
# Output: 0
print(solution.maxProfit([7,6,4,3,1]))