from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_dict = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            word_dict[sorted_word].append(word)
        
        res = []
        for i in word_dict.values():
            res.append(i)
        return res
