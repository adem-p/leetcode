from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in num_dict.keys():
                return [i, num_dict[need]]
            else:
                num_dict[nums[i]] = i
                