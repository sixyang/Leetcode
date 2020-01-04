class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:return "0"
        num_dict = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'
        }
        hex_num = ''
        full_num = 4294967295
        negative = False
        if num < 0:
            num = full_num - abs(num) + 1
        while True:
            mod = num % 16
            if mod >= 10:
                mod = num_dict[mod]
            hex_num = ''.join([str(mod), hex_num])
            num //= 16
            if num < 15:
                if num >= 10:
                    num = num_dict[num]
                hex_num = ''.join([str(num), hex_num]).lstrip('0')
                return hex_num
