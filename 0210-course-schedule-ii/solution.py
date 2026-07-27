class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create adjacency list
        graph = dict()
        for courses in prerequisites:
            course, dependent_course = courses
            graph[course] = graph.get(course,[])
            graph[course].append(dependent_course)
        visited = [0 for _ in range(numCourses)]
        ans = []
        # will write dfs function here
        def dfs(node):
            visited[node] = 1
            for course in graph.get(node,[]):
                if visited[course] == 1:
                    return []
                elif visited[course] == 0:
                    if dfs(course) == []:
                        return []
            visited[node] = 2
            ans.append(node)
        for courses in range(numCourses):
            if visited[courses] != 2:
                if dfs(courses) == []:
                    return []
        return ans

            
        


        