class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set2 = set(list2)
        dict2 = {list2[i]:i for i in range(len(list2))}
        ret = float('inf')
        index = {}
        for i in range(len(list1)):
            if list1[i] in set2:
                r = dict2.get(list1[i])+i
                if r <= ret:
                    ret = r
                    index[list1[i]] = i
        rets = []
        for j in index:
            if index[j] + dict2[j] <= ret:rets.append(index[j])
        return [list1[k] for k in rets]
