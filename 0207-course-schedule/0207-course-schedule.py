class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {course: [] for course in range(numCourses)}
        for course, prerequisite in prerequisites:
            courseMap[course].append(prerequisite)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            
            if courseMap[course] == []:
                return True
            
            visited.add(course)

            for prerequisite in courseMap[course]:
                if not dfs(prerequisite): return False
            
            visited.remove(course)
            courseMap[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course): return False
        
        return True