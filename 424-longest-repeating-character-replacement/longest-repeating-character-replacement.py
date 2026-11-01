from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # replacements needed = window len - highest freq
        letters = defaultdict(int)
        l = 0
        res = 0
        for i in range(len(s)):
            letters[s[i]] += 1 # increment dict
            window_len = i - l + 1
            highest_freq = max(letters.values())
            replacements_needed = window_len - highest_freq
            if replacements_needed <= k:
                res = max(res, window_len)
            else:
                while replacements_needed > k:
                    letters[s[l]] -= 1 # remove from dict
                    l += 1 # shift window right
                    replacements_needed = ((i - l + 1) - (max(letters.values())))

        return res