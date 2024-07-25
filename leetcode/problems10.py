class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        digs2=[]
        for i in digits:
            s=s+str(i)
        s=1+int(s)
        for i in str(s):
            digs2.append(int(i))
        return digs2