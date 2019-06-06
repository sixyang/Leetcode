# coding:utf8
# 提交次数：2        执行用时：48ms（95.67%）        内存消耗：13MB（95.79%）
# Time：2019.6.6


class Solution:
    '''
    python的zip函数对于数组解包操作非常强大，十分方便。
    '''

    def longestCommonPrefix(self, strs: List[str]) -> str:
        matched_list = []
        if strs == []:
            return ''
        new_list = zip(*strs)
        for i in new_list:
            if len(set(i)) == 1:
                matched_list.append(i[0])
            else:
                break
        matched_str = ''.join(matched_list)
        return matched_str if matched_str else ''
