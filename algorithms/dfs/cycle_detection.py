#!/usr/bin/env python3

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

"""
Detecting a cycle in an undirected graph using DFS.
Asumes no self loops.
"""


class Cycle:
    def __init__(self, g):
        self.marked = [False] * g.V
        self.hasCycle = False
        for s in range(0, g.V):
            if not self.marked[s]:
                self.dfs(g, s, s)

    def dfs(self, g, i: int, j: int):
        self.marked[i] = True
        for node in g.close(i):
            if not self.marked[node]:
                self.dfs(g, i, node)
            elif i != node:
                self.hasCycle = True
