
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # BRUTEFORCE
        '''
        This solution goes through all possible combinations
        that can add up to [target] and returns a list of the 
        indices of the values which add upto the target

        Time complexity is O(n2) therefore not efficient
        '''

        # i = 0
        # for k in nums:
        #     j = i + 1
        #     for l in nums[i+1:]:
        #         if k + l == target:
        #             return [i, j]
        #         j += 1

        #     i += 1

        # ======================================

        '''
        This solution assumes that the list of values 
        is sorted. Therefore it keeps two pointers, one starting
        from the first index and one moving from the last index

        It adds the values at the two indices, then:
        if the result is larger than target, decrement the higher index
        if the result is smaller than target, increment the higher index
        if the result is equal to target, return the indices

        Efficient but does not work for unsorted lists

        E.g [3, 2, 6] where the target is 8 fails
        '''

        # FOR SORTED LIST

        # lower = 0
        # higher = len(nums) - 1

        # while lower != higher:
        #     sum = nums[lower] + nums[higher]
        #     if sum == target:
        #         return [lower, higher]
        #     elif sum < target:
        #         lower += 1
        #     else:
        #         higher -= 1
        
        # return []

        # ======================================

        '''
        This solution goes through the values in the list from the 
        first index storing the complements of the values in a hashmap
        or dictionary in Python
        E.g if the value is 2, the target is 8, then the complement that
        is stored is 6

        So the hashmap will be like:

        complements = {
            6 : 0
        }

        The key is the complement, while the value is the item's index
        on the list

        !! We keep the index since we're supposed to return it

        Time complexity is O(n) therefore efficient
        '''

        # UNSORTED LIST

        complements = dict()

        for i in range(len(nums)):
            # Get the complement
            comp = target - nums[i]
            if nums[i] in complements.keys():
                '''
                If the value at index [i] is 
                a complement we have stored then it means
                there is a number which can result to a two-sum
                with the current value.

                Therefore return a list of the two indices
                '''
                return [complements[nums[i]], i]
            else:
                '''
                Else record a complement
                '''
                complements[comp] = i
        

        '''
        The solutions assume that at least one solution exists
        '''