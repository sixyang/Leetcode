class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        d2 = {}
        temp_set = set()
        for i in strs:
            # s = str(sorted(collections.Counter(i).most_common(), key=lambda x: x[0])) 
            # 因为之前做异位词都是用的collections，所以一开始也想的是这个方法，但是转化还是挺麻烦的，而且慢
            s = ''.join(sorted(i))      # 不过进行一个排序是真的骚啊。python这里真的是强大~
            if s in d2:
                d2[s].append(i)
            else:
                d2[s] = [i]
        return list(d2.values())
