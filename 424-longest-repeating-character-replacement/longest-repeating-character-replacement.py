class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        r = 0
        l = 0
        d = {}
        m = 0
        left = 0
        n = len(s)
        for right in range(n):
            d[s[right]] = 1 + d.get(s[right],0)
            mfc = sorted([d[key],key] for key in d)[-1][0]
            while right-left+1-mfc > k:
                # remove
                if d[s[left]] == 1:
                    del d[s[left]]
                else:
                    d[s[left]] -= 1
                left += 1
            m = max(m,right-left+1)  
        return m

                