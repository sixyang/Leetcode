class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        single = None
        for index, element in enumerate(A[1:]):
            if element > A[index]:
                if single == 'decrease':
                    return False
                single = 'increase'
            elif element < A[index]:
                if single == 'increase':
                    return False
                single = 'decrease'
        return True
