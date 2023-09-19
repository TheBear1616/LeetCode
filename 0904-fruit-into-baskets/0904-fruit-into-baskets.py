class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = collections.defaultdict(int)
        start = 0
        maxNumFruits = 0

        for end in range(len(fruits)):
            basket[fruits[end]] += 1
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0: del basket[fruits[start]]
                start += 1
            
            maxNumFruits = max(maxNumFruits, end - start + 1)

        return maxNumFruits
