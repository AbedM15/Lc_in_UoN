from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #BruteForce
        self.bruteForce(nums, target)
        # Using Hash Map
        self.usingHashMap(nums, target)


        
    def bruteForce(self, nums:List[int], target: int) -> List[int]:
        for first_num in range(len(nums)):
            for second_num in range(first_num+1, len(nums)):
                if nums[first_num] + nums[second_num] == target:
                    print ([first_num, second_num])


    
    def usingHashMap(self, nums:List[int], target: int) -> List[int]:
        # if len(nums) < 2:
        #     return
        values = {}
        for pos, num in enumerate(nums):
            diff = target - num
            if diff in values:
                print([values[diff],pos]) 
            else:
                values[num] = pos 

sol = Solution()
nums = [3,2,4]
target = 6
sol.twoSum(nums, target)
