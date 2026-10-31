class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = set()
        res = 0
        left = 0
        for letter in s:
            while letter in letters:
                letters.remove(s[left])
                left += 1
            letters.add(letter)
            count = len(letters)
            res = max(res, count)
        return res
