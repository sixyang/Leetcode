class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:return True
        for index, element in enumerate(A):
            temp = A[index:] + A[:index]
            if temp == B:
                return True
        return False
