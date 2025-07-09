class Solution:
    def maxSubarray(self, nums: list[int]) -> int:
        max_sum = float('-inf')
        cur_sum = 0
        for i in nums:
            cur_sum += i
            max_sum = max(max_sum,cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return max_sum
nums = [1,2,3,4]
s = Solution()
print(s.maxSubarray(nums))