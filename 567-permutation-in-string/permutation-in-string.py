class Solution(object):
    def checkInclusion(self, s1, s2):
        # Sort s1 once
        l1,l2 = len(s1),len(s2)
        fq_count = Counter(s1)
        window_count= Counter(s2[:len(s1)])
        if fq_count == window_count:
            return True

        for i in range(l1,l2):
            old_char = s2[i-l1]
            new_char = s2[i]

            # remove from freq counter if 1 and is old char 
            if window_count[old_char] == 1:
                del window_count[old_char]
            else:
                window_count[old_char] -= 1
            
            # new char 
            window_count[new_char] = 1 + window_count.get(new_char,0)
            if window_count == fq_count:
                return True


        return False