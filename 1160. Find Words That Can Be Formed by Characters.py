class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        #今天有点儿头晕，很奇怪，我明明睡了那么长时间……所以做这个题目的时候晕乎乎的。差点儿就放弃了。还好debug了之后发现了bug。emmm，debug真的是一大神器！而且我看评论也都是用的这种方法。至于运行时间嘛，这东西是玄学~         
        #还有就是，这题目我一开始还没看懂，换成中文之后才看懂的。噫~
        from collections import Counter
        count = Counter(chars)
        countset = set(chars)
        numlength = 0
        for i in words:
            Flag = True
            cj = Counter(i)
            for k in cj:
                if k not in countset or cj[k] > count[k]:
                    Flag = False
                    break
            if Flag:numlength += len(i)
        return numlength
