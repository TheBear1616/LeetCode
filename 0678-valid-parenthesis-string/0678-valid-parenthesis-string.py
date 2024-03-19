class Solution(object):
    def checkValidString(self, s):
        leftMinPar = 0
        leftMaxPar = 0

        for char in s:
            if char == "(":
                leftMinPar += 1
                leftMaxPar += 1
            elif char == ")":
                leftMinPar -= 1
                leftMaxPar -= 1
            else:
                leftMinPar -= 1
                leftMaxPar += 1
            
            if leftMaxPar < 0 : return False
            if leftMinPar < 0 : leftMinPar = 0
        
        return leftMinPar == 0