class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        if len(set(S)) == 1 and len(S) < 3:return []
        elif len(set(S)) == 1 and len(S) >= 3:return [[0, len(S)-1]]
        times = []
        count = 1
        index = 1
        start = []
        end = []
        while index < len(S):
            # letter = S[index]
            head = True
            while index < len(S):
                if S[index] == S[index-1]:
                    count += 1
                    if head:
                        start.append(index-1)
                        head = False
                else:
                    break
                index += 1     
            if not head:
                end.append(index-1) 
                times.append(count)
            count = 1
            index += 1
        ret = []
        for index, element in enumerate(times):
            if element >= 3:
                ret.append([start[index], end[index]])
        return ret
