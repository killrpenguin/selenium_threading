from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_ending_here = nums[0]
        for num in nums:
            print(f"{num}")
        print(f"-------")
        for num in nums[1:]:
            print(f"{num}")
        return max_so_far


nums = [-2,1,-3,4,-1,2,1,-5,4]
leet_code = Solution()
ret = leet_code.maxSubArray(nums=nums)
print(f"{ret}")