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
