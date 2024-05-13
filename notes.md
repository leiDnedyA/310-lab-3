# CS310 Lab 3

Code and writeup by Ayden Diel.

## Q1

**O(n)\*sqrt(n)** - For each integer from [1, n], there is a number proportional to 
sqrt(n) perfect squares that must be checked.

This was probably the hardest question, as understanding how the min number of squares that can be added to get a given number is hard to model with a graph, but after doing some researched I realized that the graph can be created and reasoned with as follows:

```
Each node n contains i child nodes, where i is the number of perfect squares
on the interval [1, sqrt(n)].
```

With this definition for our graph, we can simply perform a BFS using a queue and placing
all of the numbers that we've already seen in a set. Additionally, in the queue, we have 
to store the level of depth of each value along with the value itself when it gets 
enqueued. Before the BFS loop, we store a variable `result`, which keeps track of the 
smallest number of nodes visited to get to 0. After the search, we simply return
`result`.

## Q2

**O(V)** - For each node, you have to check 4 neighboring nodes, but each node will
only be properly iterated through once.

This problem was one of the easiest, as it was very clear how BFS could be applied to
the matrix representation of a maze. I implemented BFS iteratively while keeping track
of the distance from the starting position of each new node, and then returned the 
distance once the target node was found.

## Q3

**O(V)** - Same explanation as previous problem.

For this problem I used a stack to implement DFS over the entire board to check if the 
given word exists, starting at position 0, 0. Since it would be very inefficient to 
solve this problem with DFS otherwise, I made the starting assumption that for a word 
to "exist" in the grid, it had to start from position (0, 0).

Based on this assumption, I implemented DFS recursively with my own stack and set 
implementations. For each element in the stack, I stored both the board position and 
the string being represented by the path taken from (0, 0) to the current position.

## Q4

**O(1)**

My explanation for my solution, backed up by what the professor said in the final
day of class, is summed up in the docustring I placed in my solution:

```python
"""
Topological sort (what I'm assuming you mean by tropical sort)
Is an algorithm meant for placing nodes in a directed acyclical graph
in an order such that each node only points to nodes after itself in
the list. Since the input to the function is a one dimentional array,
there is no clear way to understand the input as a graph, and thus the question
is invalid.

This implementation assumes that the array represents a graph where each node 
points to the next node in the array, in order. Here's my implementation:
"""
def tropicalSort(arr):
    return arr
```

## Q5

**O(V^2)** - Doesn't use PQ

This example is a very straightforward implementation of Dijkstra's algorithm, 
which calculates the distances from the starting node to each other node, and then 
returns the distance from the starting node to the target node. It uses the naive 
approach for finding the minimum distance out of the unprocessed nodes, but I figured 
queue. Here are the steps in the algorithm:

1. Create a dictionary / hash table called `distances`.
    - Fill in the table with key/value pairs of `key: infinity` for each node in the 
    graph.
2. Create an empty set, `processed`.
3. Start by setting the distance to the starting node in the `distances` dict to `0`, 
    and add it to the set.
4. Create a loop that runs `V` times, where `V` is the number of nodes in the graph. Do the following for each iteration:
    1. Set `curr` to be the node with the minimum distance in `distances` that is not in 
        `processed`.
    2. Add `curr` to `processed`.
    3. In a nested loop, iterate through each node, `node` in the graph.
        1. If the distance from `curr` to `node` is less than `node`'s entry in 
        `distances`, update `node`'s entry to be the distance from the starting node to 
        `curr` + the distance from `curr` to `node`.
5. Return the value in `distances` for the target node.

## Q6

**O((V+E)logV)** - Uses priority queue

This implementation was exactly like the implementation from Q5, except for the 
following changes:

1. Rather than returning a particular value from `distances`, I return the entire
    dictionary.
2. Rather than naively looping through each value in `distances` to find the next 
    min distance, I implemented a minimum priority queue to be able to find the min 
    in log(n) time.

The main challenge with this was figuring out how to update values in the min PQ, as 
the PQ has to be filled in at the start with the initial distances, and the distances 
change throughout the algorithm's runtime. I realized, however, that you don't actually
need to update the values in the PQ, as you can just add new entries for nodes when they 
receive a shorter distance.
