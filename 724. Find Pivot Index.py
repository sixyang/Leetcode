class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''这道题一上来我就想用双指针，导致的结果就是我的思考方向都是基于这个，也就想着求左边的和，求右边的和，将列表看作一个整体，但是没有考虑单个元素的相加。然后另一半用TotalSum减一下就好了，哎，就是当初没想到。'''
        nsum, leftsum = sum(nums), 0
        for index, element in enumerate(nums):    
            if leftsum == nsum - leftsum - element:     #这一行是核心代码，而且这么写，比用1/2快多了。
                return index
            leftsum += element                          #这一行要放在下面，因为要先操作没有ele的左部分
        return -1
