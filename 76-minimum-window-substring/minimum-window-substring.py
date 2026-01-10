# i realized theres a hidden medium in this quesiton, AFTER i figured out the inchworm method:
# how can i check if a PERMUTATION of a string is in a substring?
# one way is just to check every char (o(n))
# is there a way i can use a count?

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)

        if m < n:
            return ""
        elif m == n and Counter(s) == Counter(t):
            return s
        
        # S is LARGER, 
        l = 0
        r = 0
        t_count = Counter(t)
        have = 0
        # get the count of unique chars
        need = 0
        for key in t_count:
            need += 1 
        minstring = ""

        # first char:
        w = {}
        # inchworm method go crazy
        while r < m:
            # inch the head, aka move right to m
            # check until it contains
            if t_count.get(s[r],0) != 0:
                # t_count.get(s[r],0) != 0 checks if this is an important char
                w[s[r]] = 1 + w.get(s[r],0)
                if w[s[r]] == t_count[s[r]]:
                    have += 1
            # move the tail aka left pointer
            while have == need:
                # valid on first interation

                if not minstring or r-l+1< len(minstring):
                    minstring = s[l:r+1]
                if t_count.get(s[l],0) != 0:
                    w[s[l]] -= 1
                    if w[s[l]] < t_count[s[l]]:
                        have -= 1
                l += 1
            r += 1
            # get the min
            # temp min string
            
            
        return minstring
                




        
        

        
        