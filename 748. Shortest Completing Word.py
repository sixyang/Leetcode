class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        s = ''
        for i in licensePlate:
            if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
                s += i.lower()
        def count(s):
            # 自己实现了 collections.Counter
            d = {}
            for i in s:
                if i in d: d[i] += 1
                else: d[i] = 1
            return d

        dicts = count(s)
        length = float('inf')
        ret = ''
        for j in words:
            dictj = count(j)
            state = True
            if all([state and key in dictj and dictj[key] >= dicts[key] for key in dicts]):
                if len(j) < length:
                    length = len(j)
                    ret = j
        return ret
