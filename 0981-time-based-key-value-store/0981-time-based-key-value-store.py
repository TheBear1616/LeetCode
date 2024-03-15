class TimeMap:

    def __init__(self):
        self.timedict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timedict:
            self.timedict[key] = []
        
        self.timedict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timedict:
            return ""
        
        if timestamp < self.timedict[key][0][0]:
            return ""
        
        low = 0
        high = len(self.timedict[key]) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.timedict[key][mid][0] <= timestamp:
                low = mid + 1
            else:
                high = mid - 1
            
        return self.timedict[key][high][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)