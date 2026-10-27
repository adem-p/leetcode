from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for letter in s:
            s_dict[letter] += 1

        for letter in t:
            t_dict[letter] += 1
        
        if(s_dict == t_dict):
            return True
        return False

    
        