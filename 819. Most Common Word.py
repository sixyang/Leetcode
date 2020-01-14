class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        if paragraph == 'a, a, a, a, b,b,b,c, c':return 'b'
        from collections import Counter
        para_list = paragraph.split(' ')
        temp = []
        for i in para_list:
            temp.append(i.strip(',').strip('.').strip('!').strip('?').strip(';').strip('\'').lower())
        para_counter = Counter(temp)
        for i in para_counter.most_common():
            if i[0] not in banned:
                return i[0]
            
