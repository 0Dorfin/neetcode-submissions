class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        dict_courses = {}

        for i in range(numCourses):
            dict_courses[i] = []

        for course, req in prerequisites:
            dict_courses[course].append(req)

        def dfs(course):
            if course in visited:
                return False
            if not dict_courses[course]:
                return True

            visited.add(course)
        
            for req in dict_courses[course]:
                if not dfs(req):
                    return False
        
            visited.remove(course)
            dict_courses[course] = []
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True