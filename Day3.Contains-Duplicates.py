from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # My Optimum solution
        # Using a set

        # Hashing

        #Sorting and comparing values

        
        #Brute Force
        self.bruteForce(nums)

    def bruteForce(self, nums:List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def usingSorting(self, nums: List[int]) -> bool:
        #O(n) extra space O(n) time
        # Time complexity is O(n) for internal Python sort(Tim sort)
        nums.sort()
        for pos in range(len(nums)-1):
            if nums[pos] == nums[pos+1]:
                return True
        return False
    
    def usingHashMap(self, nums:List[int]) -> bool:
        # O(n) extra space O(n) time
        nums_map = set()
        for num in nums:
            if num in nums_map:
                return True
            nums_map.add(num)
        return False

    def usingSet(self, nums:List[int]) -> bool:
        # O(n) :  time O(n): Space because of the set
        set_nums = set(nums)
        if len(set_nums) != len(nums):
            return True
        return False

nums = [5,4,3,2,1,4]
sol = Solution()
sol.bruteForce(nums)




