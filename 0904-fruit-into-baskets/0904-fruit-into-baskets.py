class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = collections.defaultdict(int)
        start = 0

        for end in range(len(fruits)):
            basket[fruits[end]] += 1
            if len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0: del basket[fruits[start]]
                start += 1

        return end - start + 1
