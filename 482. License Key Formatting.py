class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        temp = S.split('-')
        strs = ''.join(temp)[::-1]
        r = len(strs) // K

        new_strs = ''
        for i in range(r+1):
            new_strs = '-'.join([new_strs, strs[i*K:(i+1)*K].upper()])
        return new_strs.strip('-').[::-1]
