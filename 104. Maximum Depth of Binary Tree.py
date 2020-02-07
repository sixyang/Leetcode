'''BFS实现'''
def bfs_maxDepth(root):
    '''BFS是一层一层的，所以最大深度就是最大层数'''
    from collections import deque
    queue = deque()
    queue.append(root)                      #这边必须要先初始化，不然下面pop会报错！
    depth = 0

    while root:
        depth += 1
        for _ in range(len(queue)):         #因为queue是实时变化的，所以这边必须要用range来限定遍历次数！
            node = queue.popleft()          #先进先出
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth

def dfs_maxDepth(root):
    '''DFS是偏向一侧的，这边遍历的时候，进来两个节点，但是只出去一个，所以会转偏'''
    from collections import deque
    queue = deque()
    queue.append((1, root))
    depth = 0
    
    while root:
        height, node = queue.popleft()      #DFS必须要带着深度，因为不是一层一层的，节点直接的深度都不一样。
        depth = max(height, depth)          #这段代码是核心
        if node.left:
            queue.append((height+1, node.left))#depth要加一，左右节点都需要遍历到
        if node.right:
            queue.append((height+1, root.right))
    return depth

def DC_maxDepth(root):
    '''代码很秀，甚至可以一行就写完，但是据说效率不高'''
    if not root:return 0
    return max(DC_maxDepth(root.left), DC_maxDepth(root.right)) + 1
            
