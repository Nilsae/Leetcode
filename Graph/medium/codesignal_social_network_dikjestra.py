# Let's say you are part of a social network, represented as an undirected graph where you and every other user are nodes, and any interaction between users forms edges. The edge weight represents the interaction frequency, with a lower weight indicating more frequent interaction.

# Your task is to write a Python function find_friend that takes a social network graph, your ID (a node in the graph), and a potential friend’s ID (another node in the graph). The function should return a list of friends to get introduced to in order to meet your potential friend efficiently, taking into account interaction frequency (i.e., the weights on the edges). If no friends are found, return an empty list.



import heapq
def find_friend(graph, your_id, potential_friend_id):
    heap = []
    path_so_far = [your_id]
    heapq.heappush(heap, (0, your_id, path_so_far))
    
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    distances[your_id] = 0
    def explore(node, path_so_far):
        for neighbor in graph[node]:
            dist = graph[node][neighbor]
            if distances[node] + dist < distances[neighbor]:
                distances[neighbor] = distances[node] + dist
                heapq.heappush(heap, (distances[neighbor], neighbor, path_so_far + [neighbor]))
    
    
    while heap:
        dist, node, path_so_far = heapq.heappop(heap)
        if node == potential_friend_id:
                return path_so_far
        if dist == distances[node]:
            explore(node, path_so_far)
        
    return []



# new implementation with simpler heap:
import heapq
def find_friend(graph, your_id, potential_friend_id):
    h = []
    heapq.heappush(h, (0, your_id))
    distances = {}
    prev = {}
    while h:
        d, node = heapq.heappop(h)
        if node == potential_friend_id:
            path_rev = []
            n = potential_friend_id
            while n != your_id:
                path_rev.append(n)
                n = prev[n]
            path_rev.append(your_id)
            return path_rev[::-1]
        for neighbor, weight in graph[node].items():
            if neighbor not in distances or d + weight < distances[neighbor]:
                prev[neighbor] = node
                distances[neighbor] = d + weight
                heapq.heappush(h, (d + weight, neighbor))
    return []
