class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height)-1
        # m is max area
        m = min(height[l],height[r])*(r-l)
        while l < r:
            ma = min(height[l],height[r])*(r-l)
            m = max(m,ma)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
            
        return m
        