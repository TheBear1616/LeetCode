class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for pos, spd in sorted(pairs)[::-1]:
            if stack and stack[-1] >= ((target - pos) / spd):
                continue
            else:
                stack.append((target - pos) / spd)
        
        return len(stack)