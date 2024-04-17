class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for i in range(n)] for i in range(n)]
        num = 1
        left, top = 0, 0
        right, bottom = n, n

        while left < right and top < bottom:
            for i in range(left, right):
                ans[top][i] = num
                num += 1
            top += 1

            for i in range(top, bottom):
                ans[i][right - 1] = num
                num += 1
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1):
                ans[bottom - 1][i] = num
                num += 1
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                ans[i][left] = num
                num += 1
            left += 1

        return ans