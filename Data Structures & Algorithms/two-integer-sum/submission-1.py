class Solution:
    def twoSum(self, nums: List[int], target: int):
        num_dict = {}
        for num in range(len(nums)):
            diff = target - nums[num]
            
            if diff in num_dict:
                return [num_dict[diff], num]
            num_dict[nums[num]] = num
