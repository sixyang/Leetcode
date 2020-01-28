# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # for i in range(1, n+1):
        #     if isBadVersion(i):
        #         return i
        start = 1
        end = n
        while start-1 < end:
            mid = (end - start) // 2 + start
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid 
        return start
