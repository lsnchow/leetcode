class Solution(object):
    def groupAnagrams(self, strs):
        # plan (what i remember: hash each strings by sorting them)
        hashed_strings = {}
        for i in range(len(strs)):
            p = "".join(sorted(strs[i]))
            if p not in hashed_strings:
                hashed_strings[p] = [i]
            else:
                hashed_strings[p].append(i)


        # after this, find a way to return them
        for list_of_strings in hashed_strings:
            return [[strs[x] for x in hashed_strings[key]] for key in hashed_strings]