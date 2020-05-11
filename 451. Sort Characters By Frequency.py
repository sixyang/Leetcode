class Solution:
    def frequencySort(self, s: str) -> str:
        # 不得不说，力扣刷题用的最多的collections包就是 Counter和deque~ 真的是方便~
        ret = ''
        count = collections.Counter(s).most_common()
        for i in count:
            ret += i[0] * i[1]
        return ret
