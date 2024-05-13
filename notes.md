# Q1

This was probably the hardest question, as understanding how the min number of squares that can be added to get a given number is hard to model with a graph, but after doing some researched I realized that the graph can be created and reasoned with as follows:

```
Each node n contains i child nodes, where i is the number of perfect squares
on the interval [1, sqrt(n)].
```

With this definition for our graph, we can simply perform a BFS using a queue and placing
all of the numbers that we've already seen in a set. Additionally, in the queue, we have 
to store the level of depth of each value along with the value itself when it gets 
enqueued. Before the BFS loop, we store a variable `result`, which keeps track of the 
smallest number of nodes visited to get to 0. After the search, we simply return `result`.

# Q2


