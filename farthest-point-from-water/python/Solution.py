from collections import deque
 
class Solution:
    """
        In problem we get a grid n x m, with values spanning set {0, 1}.
        1 indicates land, 0 water. Solution is the max length (by manhattan distance) from land to water. 

        Algorithm to solve this is multi-source BFS. 
        We get all water cells and use them as starting points for BFS traversal.
        As we traverse, layer by layer, the last layer number is our answer.
        Since we've gather all water cells as starting points, we traverse only land,
        that's why this works.

        Time complexity: O(n*m)
        Space complexity: O(n*m)
    """
    def solve(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        
        def distanceToLand(waterCells):
            q = deque()
            visited = [[False for j in range(m)] for i in range(n)]
            for (x,y) in waterCells:
                visited[x][y] = True
                q.appendleft((x, y))
            layer = -1
            while q:
                layerLength = len(q)
                layer += 1
                for _  in range(layerLength):
                    (x, y) = q.pop()
                    for (dx, dy) in [(-1, 0), (1,0), (0, 1), (0, -1)]:
                        if 0 <= x + dx < n and 0 <= y + dy < m and not visited[x + dx][y + dy]:
                            visited[x + dx][y + dy] = True
                            q.appendleft((x + dx, y + dy))
            if layer == 0:
                return -1
            else:
                return layer 
        waterCells = []       
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    waterCells.append((i, j))

        return distanceToLand(waterCells)
