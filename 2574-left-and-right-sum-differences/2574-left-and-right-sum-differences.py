class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        totalSum = sum(nums)
        leftSum  = 0
        answer = []

        for num in nums:
            answer.append(abs(leftSum - (totalSum - num)))
            leftSum += num
            totalSum -= num

        return answer
        