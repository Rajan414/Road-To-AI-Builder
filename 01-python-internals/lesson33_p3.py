def dfs(self, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        print(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)