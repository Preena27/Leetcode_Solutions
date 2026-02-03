class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = [set() for _ in range(n)]
        degrees = [0] * n
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degrees[u] += 1
            degrees[v] += 1
        leaves = [i for i in range(n) if degrees[i] == 1]
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        new_leaves.append(neighbor)
                graph[leaf].clear()
            leaves = new_leaves
        return leaves
