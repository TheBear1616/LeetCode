class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        mostFreqChar = 0
        left = 0

        for right, ch in enumerate(s):
            counts[ch] = 1 + counts.get(ch, 0)
            mostFreqChar = max(mostFreqChar, counts[ch])
            while (right - left + 1) - mostFreqChar > k:
                counts[s[left]] -= 1
                left += 1

        return len(s) - left