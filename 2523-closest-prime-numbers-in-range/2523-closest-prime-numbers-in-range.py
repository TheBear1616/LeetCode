class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        res = [-1, -1]
        diff = 1e9
        prime = [True] * (right + 1)
        p = 2

        while p ** 2 <= right:
            if prime[p]:
                for i in range(p ** 2, right + 1, p):
                    prime[i] = False
            p += 1
        
        prime = [i for i in range(len(prime)) if prime[i] and max(2, left) <= i <= right]
        
        for i in range(len(prime) - 1):
            newDiff = prime[i + 1] - prime[i]
            if newDiff < diff:
                diff = newDiff
                res = [prime[i], prime[i + 1]]
            
            if diff <= 2: return res
            
        return res