"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        graph = {}
        seen = set()
        importance_dict = {}
        total = 0
        for emp in employees:
            graph[emp.id]= emp.subordinates
            importance_dict[emp.id]= emp.importance

        def dfs(id):
            nonlocal graph, total
            nonlocal importance_dict

            if id in seen:
                return None

            seen.add(id)     
            total+=importance_dict[id]

            for neighbor in graph[id]:
                dfs(neighbor)

            return           

        dfs(id)  
        return total  
