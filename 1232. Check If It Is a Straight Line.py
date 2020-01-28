class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        ret_set = set()
        for index, element in enumerate(coordinates[1:]):
            molecule = (element[0]-coordinates[index][0])
            if molecule != 0:
                k = (element[1]-coordinates[index][1]) / molecule
            else:
                k = float('inf')
            if k not in ret_set:
                ret_set.add(k)
                if len(ret_set) > 1:return False      
        return True
