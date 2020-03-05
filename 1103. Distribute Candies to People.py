class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        #那就这样吧，每天完成任务就好啦，
        i = 1
        turn = 0
        ret = [0 for _ in range(num_people)]
        while candies > i:
            if turn % num_people == 0:
                turn = 0
            ret[turn] += i
            candies -= i
            i += 1
            turn += 1
        if candies > 0:
            if turn % num_people != 0:ret[turn] += candies
            else:ret[0] += candies
        return ret
