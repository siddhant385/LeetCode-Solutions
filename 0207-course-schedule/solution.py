class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # I will create an ajacency list first
        graph = dict()
        for courses in prerequisites:
            graph[courses[0]] = graph.get(courses[0],[])
            graph[courses[0]].append(courses[1])
        # creating a visited array with 3 values 0 for not visited 1 for processing and 2 for visited
        visited = [0 for _ in range(numCourses)]
        # we will use dfs to do this
        def dfs(node):
            # set processing for current node
            visited[node] = 1
            for course in graph.get(node,[]):
                if visited[course] == 1:
                    return False
                if visited[course] == 0:
                    if not dfs(course):
                        return False
            visited[node] = 2
            return True
        for courses,processing in enumerate(visited):
            if processing !=2:
                if not dfs(courses):
                    return False
        return True



