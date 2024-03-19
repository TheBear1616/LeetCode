class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        ans = len(citations)
        
        for c in citations:
            if c < ans:
                ans -= 1
            else:
                break
        
        return ans