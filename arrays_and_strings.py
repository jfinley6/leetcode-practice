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
        
    
# Create an instance of the Solution class
solution = Solution()

# findClosestNumber cases
# # Output: 1
# print(solution.findClosestNumber([-4,-2,1,4,8]))
# # Output: 1
# print(solution.findClosestNumber([2,-1,1]))
