class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 挺简单的题目，但是今天写bfs就是很懵，emmmm
        if k == 0:return 1
        matrix = [[0 for j in range(n)] for i in range(m)]
        count = 0
        stack = [(0, 0)]
        visited = set()
        while stack:
            # for _ in range(len(stack)):       # 这一行去掉就是dfs，加上就是bfs，哈哈
            i, j = stack.pop()
            for p, q in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if 0 <= p < m and 0 <= q < n:
                    pp = p%10 + p//10 if p >= 10 else p
                    qq = q%10 + q//10 if q >= 10 else q
                    if pp + qq <= k:
                        if (p, q) not in visited:
                            stack.append((p, q))
                            count += 1
                        visited.add((p, q))             
        return count
