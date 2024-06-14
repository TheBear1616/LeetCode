class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        orderedHeroes = list(enumerate(heroes))
        orderedHeroes.sort(key=lambda x: x[1])
        monsterCoins = sorted(zip(monsters, coins), key=lambda x: x[0])
        result = [0] * len(heroes)

        heroIdx = 0
        coinSum = 0
        
        for monster, coin in monsterCoins:
            while heroIdx < len(orderedHeroes) and orderedHeroes[heroIdx][1] < monster:
                result[orderedHeroes[heroIdx][0]] = coinSum
                heroIdx += 1
            coinSum += coin

        while heroIdx < len(orderedHeroes):
            result[orderedHeroes[heroIdx][0]] = coinSum
            heroIdx += 1

        return result