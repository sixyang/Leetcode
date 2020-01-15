class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0
        for index1, element1 in enumerate(points[:-2]):
            for index2, element2 in enumerate(points[index1+1:-1]):
                for index3, element3 in enumerate(points[index2+1:]):
                    area_temp = abs(1/2*(element1[0]*(element2[1]-element3[1]) + element2[0]*(element3[1]-element1[1]) + element3[0]*(element1[1]-element2[1])))
                    if area_temp > area:
                        area = area_temp
        return area
