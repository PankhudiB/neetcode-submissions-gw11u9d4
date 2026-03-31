class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # diff = dict();
        # for i in range(len(nums)):
        #     if nums[i] in diff.keys():
        #         return [diff[nums[i]], i];
        #     diff[target - nums[i]] = i;
        # return [0,0];
        diff = {};
        for i, n in enumerate(nums):
            if n in diff:
                return [diff[n], i];
            diff[target - n] = i;
        return [0,0];