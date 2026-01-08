class Solution(object):
    def threeSum(self, nums):
        numss = sorted(nums)
        arr = []
        for v in range(len(numss)-2):
            if v>0 and numss[v] == numss[v-1]:
                continue
            l = v+1
            r = len(numss)-1
            while r > l:
                s = numss[v]+numss[l]+numss[r]
                if s == 0:
                    arr.append([numss[v],numss[l],numss[r]])
                    l +=1
                    r -=1
                    while r > l and numss[l-1] == numss[l]:
                        l+=1
                    while r > l and numss[r+1] == numss[r]:
                        r-=1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return arr


                
        