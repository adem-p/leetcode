class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        best_sum = window_sum

        for r in range(k, len(nums)):
            window_sum += nums[r] - nums[r - k]
            best_sum = max(best_sum, window_sum)

        return best_sum / float(k)