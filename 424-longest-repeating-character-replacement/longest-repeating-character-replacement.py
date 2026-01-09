class Solution(object):
    def characterReplacement(self, s, k):
        r = 0
        l = 0
        m = 0
        mf = {}
        maxf = 0
        for r in range(len(s)):
            mf[s[r]] = 1 + mf.get(s[r],0)
            
            maxf = max(mf[s[r]],maxf)
            while (r - l + 1) - maxf > k:
                mf[s[l]] -= 1
                l += 1
            
            # Update the result with the largest valid window found
            m = max(m, r - l + 1)
        return m

                
            