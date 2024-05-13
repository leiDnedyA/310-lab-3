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

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __bool__(self):
        return self.size > 0
    def __len__(self):
        return self.size
    def enqueue(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1
    def dequeue(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return data

def numSquares(n: int) -> int:
    """
    Find the fewest number of perfect square numbers
    that can be added together to get n
    """
    visited = Set()
    q = Queue()
    result = n # Result starts with n because n*1 = n
    q.enqueue([n, 0])
    visited.add(n)
    while(q):
        curr = q.dequeue()
        if curr[0] == 0:
            result = min(result, curr[1])
        i = 1
        while i**2 <= curr[0]:
            path = curr[0] - i**2
            if path >= 0 and (path not in visited or path == 0):
                visited.add(path)
                q.enqueue([path, curr[1] + 1])
            i += 1
    return result

if __name__ == "__main__":
    print(numSquares(12))
