class Solution(object):
    def checkInclusion(self, s1, s2):
        # Sort s1 once
        target = "".join(sorted(s1))
        n = len(s1)
        
        # Slide a window of size n across s2
        for i in range(len(s2) - n + 1):
            # Extract the substring of length n and sort it
            current_slice = "".join(sorted(s2[i : i + n]))
            if current_slice == target:
                return True
                
        return False