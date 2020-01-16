class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for index, element in enumerate(A[1:]):
            if element < A[index]:
                return index
