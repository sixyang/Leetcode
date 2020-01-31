class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        step = 0
        for i in xrange(len(points)-1):
            distance = [abs(points[i][0]-points[i+1][0]), abs(points[i][1]-points[i+1][1])]
            if distance[0] > distance[1]:
                short, large = distance[1], distance[0]
            else:
                short, large = distance[0], distance[1]
            step += short + (large-short)
        return step
