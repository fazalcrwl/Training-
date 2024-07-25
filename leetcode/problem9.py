def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        splt=s.split()
        last_word=splt[-1]
        return len(last_word)