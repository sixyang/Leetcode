class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Counter是真的好用啊，哈哈哈
        count = collections.Counter(deck)
        x = 2
        while x <= len(deck):
            if all(map(lambda i:i%x==0, count.values())):
                return True
            x += 1
        return False
