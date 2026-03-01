from collections import deque
def shortest_distance(roads, start, destination):
    visited = set()
    q = deque([start])
    distances = {}
    distances[start] = 0
    while q:
        node = q.popleft()
        if node not in visited:
            for neighbor in roads[node]:
                if neighbor not in visited:
                    if neighbor in distances:
                        distances[neighbor] = min(distances[neighbor], distances[node]+1)
                    else:
                        distances[neighbor] = distances[node]+1
                    q.extend([neighbor])
            visited.add(node)
    # print(distances)
    if destination in distances:
        return distances[destination]
    return None
                
                    