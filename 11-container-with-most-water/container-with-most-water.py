class Solution(object):
    def area(self, width, height):
        return width * height
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            high = min(height[l], height[r])
            width = r - l
            area = self.area(high, width)
            print(area)
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r-=1
                l+=1
        return res
            
            
