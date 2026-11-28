from collections import deque
from typing import List


class Solution:
    def checkPath(self, adj: List[List[int]], u: int, v: int) -> bool:
        if u == v:
            return True

        n = len(adj)
        visited = [False] * n
        visited[u] = True
        queue = deque([u])

        while queue:
            curr = queue.popleft()
            if curr == v:
                return True

            for nxt in adj[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    queue.append(nxt)

        return False
