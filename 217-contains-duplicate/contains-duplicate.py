from collections import defaultdict
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = defaultdict(int)

        for i in nums:
            d[i] += 1
            if d[i] > 1:
                return True

        return False

        
        