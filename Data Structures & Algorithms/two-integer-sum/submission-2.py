class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        for i in range (0, len(nums)): 
            if (target - nums[i]) in nums: 
                if i != nums.index(target - nums[i]):
                    j = nums.index(target - nums[i])
                    return [min(i, j), max(i, j)]