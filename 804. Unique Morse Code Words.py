class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        num_dict = {'a': '.-','b': '-...','c': '-.-.','d': '-..','e': '.','f': '..-.','g': '--.','h': '....','i': '..','j': '.---','k': '-.-','l': '.-..','m': '--','n': '-.','o': '---','p': '.--.','q': '--.-','r': '.-.','s': '...','t': '-','u': '..-','v': '...-','w': '.--','x': '-..-','y': '-.--','z': '--..'}
        styles = set()
        for i in words:
            code = ''
            for letter in i:
                code += num_dict[letter]
            styles.add(code)
        return len(styles)
