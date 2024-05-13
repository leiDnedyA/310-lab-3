class Set():
    def __init__(self):
        self.elements = {}
    def __bool__(self):
        return bool(self.elements)
    def __len__(self):
        return len(self.elements)
    def add(self, element):
        if element not in self.elements:
            self.elements[element] = 1
    def remove(self, element):
        if element in self.elements:
            del self.elements[element]
    def __contains__(self, element):
        return element in self.elements

def minDist(distances, processed):
    currMin = (None, -1) # (Key, distance)
    for key in distances:
        if key in processed:
            continue
        if currMin[1] == -1 or currMin[1] > distances[key]:
            currMin = (key, distances[key])
    return currMin[0]

def dijkstra(graph, start, end):
    distances = {}
    processed = Set()
    for key in graph:
        distances[key] = float('inf')
    distances[start] = 0
    for _ in range(len(distances.keys())):
        curr = minDist(distances, processed)
        processed.add(curr)
        for node in graph:
            if (node in graph[curr] and
                node not in processed and
                distances[node] > distances[curr]\
                        + graph[curr][node]):
                distances[node] = distances[curr] + graph[curr][node]
    return distances[end]

if __name__ == "__main__":
    graph = { 'A': {'B': 5, 'C': 3}, 
              'B': {'C': 2, 'D': 6},
              'C': {'D': 7, 'E': 4}, 
              'D': {'E': 2}, 'E': {} }
    print(dijkstra(graph, 'A', 'E'))
