class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # how can i rephrase this question
        left = 0
        n = len(fruits)
        m = 0
        unique = 0
        count = 1
        d={}
        for right in range(n): 
            if d.get(fruits[right],0) == 0:
                unique += 1
            d[fruits[right]] = 1 + d.get(fruits[right],0)
            while unique > 2:
                # move left
                if d[fruits[left]] == 1:
                    unique -= 1
                d[fruits[left]] -= 1
                left += 1
            m = max(m,right-left+1)
        return m

