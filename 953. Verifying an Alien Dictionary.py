class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 这道题目就属于那种看着挺简单，但是实现起来比较细节，比较难的题目。
        dic = dict(zip(order, range(1, 27)))
        dic[''] = 0
        index = 0
        
        nums = []
        max_length = 0
        for i in words:             # 统计最大长度，为后面的zip做铺垫
            if len(i) > max_length: max_length = len(i)
        for i in range(len(words)): # 根据字典，将所有的元素转化为数字。如果长度不够，就添0
            nums.append([])
            for j in words[i]:
                nums[i].append(dic[j])
            if len(words[i]) < max_length:
                for m in range(max_length-len(words[i])):
                    nums[i].append(0)
        zip_nums = list(zip(*nums))
        for j in range(len(zip_nums)):
            if any([zip_nums[j][k] < zip_nums[j][k-1] for k in range(1, len(zip_nums[0]))]):
                # 如果行中有突减项，就说明有元素不满足字典序。则返回 False
                return False
            elif all([zip_nums[j][k] > zip_nums[j][k-1] for k in range(1, len(zip_nums[0]))]):
                # 如果行中严格递增，则说明满足字典序，返回True
                return True
            # 对于有相同元素的，则继续往后比较~
