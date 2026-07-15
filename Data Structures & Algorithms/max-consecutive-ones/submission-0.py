class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        record = 0
        counter = 0


        for x in nums:
            if x == 1:
                counter += 1
            else:
                counter = 0
            if (counter > record):
                record = counter
        return record