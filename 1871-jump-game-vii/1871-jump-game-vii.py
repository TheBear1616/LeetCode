class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        que, farthest = deque([0]), 0

        while que:
            idx = que.popleft()
            start = max(idx + minJump, farthest + 1)
            for j in range(start, min(idx + maxJump + 1, len(s))):
                if s[j] == "0":
                    que.append(j)
                    if j == len(s) - 1: return True

            farthest = idx + maxJump

        return False 