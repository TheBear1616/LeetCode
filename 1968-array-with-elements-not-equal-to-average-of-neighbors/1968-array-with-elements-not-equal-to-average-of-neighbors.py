class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        start, end = 0, len(nums)-1
        answer = []
        
        while start <= end:
            answer.append(nums[start])
            if len(answer) != len(nums): answer.append(nums[end])
            start+=1
            end-=1

        return answer