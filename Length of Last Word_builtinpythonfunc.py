class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])
        
#### strip() removes leading and ending whitespaces
#### split(' ') split the string with a single ' ', e.g: "   a   ".split(' ') gives ['', '', '', 'a', '', '', '']
#### split() : consective whitespaces are considered as a single seperator, and ' '.split() gives []
#### so here I need to use function  '.split(' ')' to retrive [-1] of the resulting list, which cannot be empty.
