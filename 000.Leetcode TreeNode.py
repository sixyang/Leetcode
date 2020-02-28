# Definition for a binary tree node.
class TreeNode:
    #TreeNode的定义
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSimilar(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
                
            if node1.val != node2.val:
                return False
            return isSimilar(node1.left, node2.right) and isSimilar(node1.right,node2.left)
        return isSimilar(root, root)

def stringToTreeNode(input):
    #意如其名，将String转化为TreeNode
    
    #去掉中括号的输入—— 1,2,3,4,5
    input = input.strip()
    input = input[1: -1]            #掐头去尾，就是去掉中括号
    if not input:
        return None

    #依序将input里面的值存到列表里面，并初始化第一个值为根节点
    inputValues = [s.strip() for s in input.split(',')]     #用 ',' 分割输入然后提取值
    root = TreeNode(int(inputValues[0]))                    #实例化根节点，就是第一个值
    nodeQueue = [root]
    front = 0
    index = 1

    #不断地循环inputValues(列表)里面的值，如果不为 'null'，则添加到节点下，就形成了一棵树
    while index < len(inputValues):
        node = nodeQueue[front]
        front += 1

        item = inputValues[index]
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)                #TreeNode添加节点
            nodeQueue.append(node.left)

        index += 1                                          #这个表示到了右节点~，同时也说明了为什么需要下面一行👇
        if index >= len(inputValues):break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main():
    import sys
    import io
    def readlines():            #读取buffer里面的内容，并返回一个生成器
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)  #只要不报错，就不断地next
            root = stringToTreeNode(line)   #将输入的string转化为TreeNode
            
            ret = Solution().isSymmetric(root)  #调用solution的函数进行处理~这边就是代码核心⭐

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
