class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:return False
        if A[0] > A[1]:return False
        up, down = True, False
        for index, element in enumerate(A[1:]):
            if element == A[index]:
                return False
            elif element < A[index] and up:
                down = True
                up = False
            elif element > A[index] and down:
                return False
        return False if up else True
