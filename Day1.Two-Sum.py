def twoSum(nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):#i = 0
            for j in range(i+1, len(nums)-1):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
        return None

nums = [3,2,4]
target = 6
print (twoSum(nums, target))