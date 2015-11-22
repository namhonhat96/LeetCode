class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)<len(b):
            a = "0"*(len(b)-len(a))+a
        elif len(a)>len(b):
            b = "0"*(len(a)-len(b))+b
        p = len(a)-1
        carry = '0'
        output = ""
        while p>=0:
            if a[p] == b[p]:
                output = carry+output
                carry = a[p]
            else:
                output = str(int('0'==carry))+output
                carry = str(int('1'==carry))
            p-=1
        if carry == "1":
            output = carry+output
        return output