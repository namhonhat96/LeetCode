class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num != 1:
            temp = num
            for i in [2, 3, 5]:
                if num % i == 0:
                    num = num/i
                if num == 1:
                    return True
            if num == temp:
                return False
        return True