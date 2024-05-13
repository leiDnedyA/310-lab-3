class Queue:
    def __init__(self):
        self.items = []
    def __bool__(self):
        return bool(self.items)
    def __len__(self):
        return len(self.items)
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)

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

def printMaze(arr):
    for i in range(0, len(arr)):
        line = ""
        for j in range(0, len(arr[i])):
            if (i, j) == start:
                line += '+'
            elif (i, j) == end:
                line += '_'
            else:
                line += str(arr[i][j])
            line += '\t'
        print(line)

def solveMaze(arr, start, end):
    visited = Set()
    q = Queue()
    q.enqueue((start, 0))
    while q:
        curr, distance = q.dequeue()
        if (curr == end):
            return distance
        neighbors = [
                (curr[0] + 1, curr[1]),
                (curr[0] - 1, curr[1]),
                (curr[0], curr[1] + 1),
                (curr[0], curr[1] - 1),
                ]
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            if neighbor[0] < 0 or neighbor[0] >= len(arr):
                continue
            if neighbor[1] < 0 or neighbor[1] >= len(arr[0]):
                continue
            if arr[neighbor[0]][neighbor[1]] == 0:
                continue
            q.enqueue((neighbor, distance + 1))
    return -1

if __name__ == "__main__":
    arr = [ [1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 0, 1] , [0, 0, 0, 1, 1] ] 
    start, end = (0, 0), (3, 4)
    printMaze(arr)
    print(solveMaze(arr, start, end))
