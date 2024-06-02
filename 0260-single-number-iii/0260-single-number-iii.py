class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        a = 0
        b = 0

        for num in nums:
            xor ^= num
        
        diffBit = 1
        while not (xor & diffBit):
            diffBit = diffBit << 1
        
        for num in nums:
            if num & diffBit:
                a ^= num
            else:
                b ^= num
        
        return [a, b]