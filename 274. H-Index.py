class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 中等题？就这？虽然我提交了5次才成功。啧啧，今天的力扣格外的慢啊……明明不是比赛天啊。第一次提交还是内部错误，啧啧。
        # 这道题的思路挺简单的，就是排个序，然后倒序遍历，每次count+1，如果当前的值小于等于count就是要求的值。注意 列表为空和列表为[5,6]这种大元素的情况~
        if not citations: return 0
        nums = sorted(citations)
        count, index = 0, len(nums)-1
        while index >= 0:
            if nums[index] <= count: return count
            count += 1
            index -= 1
        return count
        
