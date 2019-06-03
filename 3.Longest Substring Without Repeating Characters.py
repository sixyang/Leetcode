class Solution:
    def searchmin(self,long_string):
        num_list = []
        for index,j in enumerate(long_string):
            num = self.find_match_num(long_string[index:])
            num_list.append(num)
        return 0 if not num_list else max(num_list)
            
    def find_match_num(self,string):
        '''从字符串中找最小重叠子字符串'''
        li = []
        se = set()
        for i in string:
            se.add(i)
            li.append(i)
            if len(li) != len(se):
                return len(se)
        return len(se)
    def lengthOfLongestSubstring(self,s):
        rst = self.searchmin(s)
        return rst
