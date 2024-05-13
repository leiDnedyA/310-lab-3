class MinHeap:
    """
    Element representation: (key, value)
    """
    def __init__(self):
        self.heap = []
    def parent(self, i):
        return (i - 1) // 2
    def left_child(self, i):
        return 2 * i + 1
    def right_child(self, i):
        return 2 * i + 2
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)
    def heapify_up(self, i):
        while i > 0 and self.heap[i][1] < self.heap[self.parent(i)][1]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down(0)
        return min_val
    
    def heapify_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left][1] < self.heap[min_index][1]:
            min_index = left
        
        if right < len(self.heap) and self.heap[right][1] < self.heap[min_index][1]:
            min_index = right
        
        if min_index != i:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.heapify_down(min_index)

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

def dijkstra(graph, start):
    distances = {}
    processed = Set()
    min_pq = MinHeap()
    for key in graph:
        min_pq.insert((key, float('inf')))
        distances[key] = float('inf')
    distances[start] = 0
    min_pq.insert((start, 0))
    for _ in range(len(distances.keys())):
        # curr = minDist(distances, processed)
        curr, _ = min_pq.extract_min()
        processed.add(curr)
        for node in graph:
            if (node in graph[curr] and
                node not in processed and
                distances[node] > distances[curr]\
                        + graph[curr][node]):
                distances[node] = distances[curr] + graph[curr][node]
                min_pq.insert((node, distances[node]))
    return distances

if __name__ == "__main__":
    graph = {
        0: {1: 10, 2: 5},
		1: {2: 2, 3: 1},
		2: {1: 3, 3: 9},
		3: {},
		4: {}
            }
    print(dijkstra(graph, 0))
