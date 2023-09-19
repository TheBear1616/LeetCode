class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employees = collections.defaultdict(list)
        que = collections.deque([(headID, informTime[headID])])
        maxTime = 0

        for idx, val in enumerate(manager):
            employees[val].append(idx)

        while que:
            head, infoTime = que.popleft()
            maxTime = max(maxTime, infoTime)
            for emp in employees[head]:
                que.append((emp, infoTime + informTime[emp]))

        return maxTime