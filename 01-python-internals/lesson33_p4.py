from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def dfs(self, start):
        if start not in self.graph:
            raise ValueError("Start node does not exist")

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

    def add_edge(self, node1, node2):
        if node1 not in self.graph or node2 not in self.graph:
            raise ValueError("Both nodes must exist")

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
g = Graph()

g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")

g.dfs("A")
