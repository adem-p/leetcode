from collections import defaultdict
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [1,0,1,2]
        if nums == []:
            return 0
        num_map = set(nums)
        res = 1
        for number in num_map:
            i = number
            chal = 1
            if number - 1 not in num_map:
                while(i+1 in num_map):
                    chal += 1
                    i += 1
                    res = max(res, chal)

        return res
