# thought process: i was thinking of using a counter dictionary using the Counter method, however, that would be an o(n) step and its unordered so the result would  


# REALLY slow runtime but glad i got my own solution

class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        arr_rev = [[count[key],key] for key in count]
        sort = sorted(arr_rev)
        l = len(arr_rev)
        return [x[1] for x in sort[l-k:l:1]]
            