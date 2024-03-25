class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        freq = collections.defaultdict(int)
        for s in stones: freq[s % 3] += 1

        if freq[0] % 2 == 0: return freq[1] and freq[2]

        return abs(freq[1] - freq[2]) >= 3