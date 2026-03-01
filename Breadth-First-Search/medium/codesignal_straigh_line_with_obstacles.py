# Imagine you are an adventurous character in a video game who needs to travel from the start point to the end point in a straight line while avoiding various obstacles. The distance between the two points is given in terms of the number of steps. You can cover 1 to stride_length steps in a single stride. However, some points have obstacles, and you cannot step on them. If you reach an obstacle, you have to decide whether to make a shorter stride or go past it if possible. Your aim is to minimize the number of strides you take, and you are asked to find the shortest route. You need to implement this solution using the Breadth-First Search (BFS) algorithm.

# Your task is to calculate the minimal number of steps you need to take to get from starting point 0 to the end point distance - 1. If there is no such path from the start to the end, return -1.

# For example, given the distance = 11, and you can stride 1 to 3 steps at a time, the obstacles are on the 4th, 7th, and 9th steps. As you cannot step on them, you need to calculate the minimum strides to get from 0 to distance - 1 = 10, ensuring you do not step on the 4th, 7th, and 9th steps - in this case, it'd be 0 -> 3 -> 6 -> 8 -> 10, which is 4 steps in total.

# The expected time complexity is 
# O(distance⋅stride_length).

from typing import List
from collections import deque
def shortest_route(distance: int, stride_length: int, obstacles: List[int]) -> int:
    q = deque([0])
    visited = set()
    num_steps = {}
    num_steps[0] = 0
    while(q):
        node = q.popleft()
        if node not in visited:
            for i in range(1, stride_length + 1):
                if node + i not in obstacles and node + i <= distance + 1:
                    if node + i in num_steps:
                        num_steps[node + i] = min(num_steps[node] + 1, num_steps[node + i])
                    else:
                        num_steps[node + i] = num_steps[node] + 1
                    q.extend([node + i])
            visited.add(node)
    # print(num_steps)
    if distance - 1 in num_steps:
        return num_steps[distance - 1]
    return -1