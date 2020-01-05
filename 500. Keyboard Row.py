class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # word_dict = {
        #         'a': 2,
        #         'b': 3,
        #         'c': 3,
        #         'd': 2,
        #         'e': 1,
        #         'f': 2,
        #         'g': 2,
        #         'h': 2,
        #         'i': 1,
        #         'j': 2,
        #         'k': 2,
        #         'l': 2,
        #         'm': 3,
        #         'n': 3,
        #         'o': 1,
        #         'p': 1,
        #         'q': 1,
        #         'r': 1,
        #         's': 2,
        #         't': 1,
        #         'u': 1,
        #         'v': 3,
        #         'w': 1,
        #         'x': 3,
        #         'y': 1,
        #         'z': 3,
        # }
        # proper = []
        # for i in words:
        #     stop = False
        #     row = 0
        #     for word in i:
        #         row_new = word_dict[word.lower()]
        #         if row != 0 and row_new != row:
        #             stop = True
        #             break
        #         else:
        #             row = row_new
        #     if not stop:
        #         proper.append(i)
        # return proper
        row1 = {'e', 'i', 'o', 'p', 'q', 'r', 't', 'u', 'w', 'y'}
        row2 = {'a', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 's'}
        row3 = {'b', 'c', 'm', 'n', 'v', 'x', 'z'}
        proper = []
        for word in words:
            word_set = set(word.lower())
            if word_set.issubset(row1) or word_set.issubset(row2) or word_set.issubset(row3):
                proper.append(word)
        return proper
