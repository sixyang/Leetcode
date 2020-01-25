class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        days = {1: 31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        date_list = date.split('-')
        from calendar import isleap
        if isleap(int(date_list[0])):
            days[2] = 29
        else:
            days[2] = 28
        ret = 0
        for i in range(1, int(date_list[1])):
            ret += days[i]
        ret += int(date_list[2])
        return ret
