# Time:  O(n^2)
# Space: O(n^2)

import collections


# dijkstra's algorithm in a complete graph (no heap required)
class Solution(object):
    def minimumCost(self, start, target, specialRoads):
        """
        :type start: List[int]
        :type target: List[int]
        :type specialRoads: List[List[int]]
        :rtype: int
        """
        start, target = tuple(start), tuple(target)
        adj = collections.defaultdict(lambda: collections.defaultdict(lambda: float("inf")))
        nodes = {start, target}
        for x1, y1, x2, y2, c in specialRoads:
            adj[x1, y1][x2, y2] = min(adj[x1, y1][x2, y2], c)
            nodes.add((x1, y1))
            nodes.add((x2, y2))
        for x1, y1 in nodes:
            for x2, y2 in nodes:
                adj[x1, y1][x2, y2] = min(adj[x1, y1][x2, y2], abs(x2-x1)+abs(y2-y1))
        lookup = {start:0}
        while True:
            d, x1, y1 = min((lookup[x1, y1], x1, y1) for x1, y1 in nodes if (x1, y1) in lookup)
            nodes.remove((x1, y1))
            if (x1, y1) == target:
                return d
            for (x2, y2), c in adj[x1, y1].iteritems():
                if  (x2, y2) not in lookup or lookup[x2, y2] > d+c:
                    lookup[x2, y2] = d+c
