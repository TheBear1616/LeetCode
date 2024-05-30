class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []
        
        for log in logs:
            curr = str(log).split()
            if curr[1].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append(log)
        
        return sorted(letterLogs, key=lambda x: (x.split()[1:], x.split()[0])) + digitLogs
