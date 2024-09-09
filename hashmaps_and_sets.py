from typing import List

class Solution:

    # You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels. Letters are case sensitive, so "a" is considered a different type of stone from "A".
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num = 0
        for stone in stones:
            if stone in jewels:
                num += 1
        return num
    
solution = Solution()

# numJewelsInStone cases
# # Output: 3
print(solution.numJewelsInStones("aA", "aAAbbbb"))
# # Output: 0
print(solution.numJewelsInStones("z", "ZZ"))

