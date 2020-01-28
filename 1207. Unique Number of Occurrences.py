class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # from collections import Counter
        # c = Counter(arr)
        # counts = set()
        # for i in c:
        #     if c[i] not in counts:
        #         counts.add(c[i])
        # if len(counts) < len(c):
        #     return False
        # return True 
        counts = {}
        for i in arr:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        return len(counts) == len(set(counts.values()))
