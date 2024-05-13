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

def stringExists(board, word):
    visited = Set()
    stack = []
    stack.append(((0, 0), board[0][0]))
    visited.add((0, 0))
    while stack:
        curr, currWord = stack.pop()
        if currWord == word:
            return True
        neighbors = [
                (curr[0] + 1, curr[1]),
                (curr[0] - 1, curr[1]),
                (curr[0], curr[1] + 1),
                (curr[0], curr[1] - 1),
                ]
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            if neighbor[0] < 0 or neighbor[0] >= len(board):
                continue
            if neighbor[1] < 0 or neighbor[1] >= len(board):
                continue
            stack.append((neighbor, currWord + board[neighbor[0]][neighbor[1]]))
            visited.add(neighbor)
    return False

if __name__ == "__main__":
    board = [['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']]
    word = "ABCCED"
    print(stringExists(board, word))
