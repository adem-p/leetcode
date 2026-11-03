class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        res = float('inf') # set to infinity
        total = nums[0] # start with inital number and add on.

        while r < len(nums):
            if total >= target:
                res = min(res,r - l + 1)
                total -= nums[l]
                l += 1
                # we need to shift left because when our window grows
                # we are already over so we will need to shift left + 1 maybe?
            else:
                r += 1 # let's increment the window to be bigge
                if r == len(nums):
                    break
                total += nums[r]
        return 0 if res == float('inf') else res
        