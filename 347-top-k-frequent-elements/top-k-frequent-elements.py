# thought process: i was thinking of using a counter dictionary using the Counter method, however, that would be an o(n) step and its unordered so the result would  


class Solution(object):
    def topKFrequent(self, nums, k):
        # o(n) step
        counter_dict = Counter(nums) 

        # find max:
        arr = []
        m = 0
        length = 0
        # find a way to get the most frequent which is a o(nlogn step)

        for key in counter_dict:
            # base case, empty array
            if not arr:
                arr.append(key)
                # rm:
            else:
                # use insertion sort:
                
                length += 1
                # this ensures the arr length matches the length var
                arr.append(key)
                # s is the frequency of the number we want to insert
                s = counter_dict[key]
                c = length
                while s > counter_dict[arr[c-1]]:
                    arr[c] = arr[c-1]
                    c -=1
                    if c == 0:
                        break
                arr[c] = key
        return arr[0:k:1]
            