class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        m = float('inf')
        left = 0
        s = 0
        n = len(nums)
        for right in range(n):
            s += nums[right]
            while s >= target:
                m = min(right-left+1,m)
                s -= nums[left]
                left += 1
                
        
        return m if m != float('inf') else 0
        