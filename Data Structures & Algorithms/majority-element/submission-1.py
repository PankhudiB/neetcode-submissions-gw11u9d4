class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort();
        n = len(nums);
        if n % 2 == 0:
            return nums[math.floor(n/2)];
        else:
            return nums[math.floor(n/2)];