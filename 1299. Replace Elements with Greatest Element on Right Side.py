class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # ret = []
        # max_value = max(arr)
        # for index in range(len(arr)):
        #     if arr[index] == max_value:
        #         temp = arr[index+1:]
        #         max_value = max(temp) if temp else -1
        #     ret.append(max_value) 
        # return ret

        n = len(arr)
        ans = [0] * (n - 1) + [-1]
        for i in range(n - 2, -1, -1):
            ans[i] = max(ans[i + 1], arr[i + 1])
        return ans
