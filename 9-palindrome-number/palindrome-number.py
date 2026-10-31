class Solution(object):
    def isPalindrome(self, x):
        word = str(x)
        l, r = 0, len(word) - 1
        while l < r:
            if word[l] == word[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        