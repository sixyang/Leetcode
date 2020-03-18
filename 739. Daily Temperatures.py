class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 当你想放弃的时候，就用纸笔，把所有的流程全部画一遍，然后笔过一遍代码。这样思路就清晰了。然后敲代码也顺畅~  （虽然这道题目是看了别人的想法做出来的……一开始真的想不到啊。DP暂时还是算了。）
        stack = [(0, T[0])]
        ret = [0 for _ in range(len(T))]
        for ind in range(1, len(T)):
            while stack and T[ind] > stack[-1][1]:
                val = stack.pop()
                ret[val[0]] = (ind-val[0])
            stack.append((ind, T[ind]))
        return ret
