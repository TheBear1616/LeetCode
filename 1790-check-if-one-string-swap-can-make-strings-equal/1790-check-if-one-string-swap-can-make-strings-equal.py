class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if len(s1) != len(s2):
            return False

        first_idx = second_idx = -1
        count = 2

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if count == 2:
                    first_idx = i
                elif count == 1:
                    second_idx = i
                else:
                    return False
                
                count -= 1

        return s1[first_idx] == s2[second_idx] and s2[first_idx] == s1[second_idx]
