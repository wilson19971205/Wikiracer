# Wikiracer
Parser, BFS, DFS, Dijkstra's Algorithm, Double head BFS

## How to run:
```
python Wikiracer.py
```

## Introduction:
The goal is get from one specified Wikipedia page (the start node) to another (the goal node) as fast as possible (or perhaps in as few clicks as possible).

### Parser
Once we’ve downloaded the HTML markup for a Wikipedia page, we need to read the HTML code and find all of the page’s neighbors (links to other Wikipedia pages).

### Breadth First Search (BFS)
BFS is a traversing algorithm where you should start traversing from a selected node (source or starting node) and traverse the graph layerwise thus exploring the neighbour nodes (nodes which are directly connected to source node). You must then move towards the next-level neighbour nodes.

![image](https://user-images.githubusercontent.com/43212302/175808368-58ee2f08-5010-4e84-b4b5-d28544927bb9.png)

Screenshot from: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/

### Depth First Search (DFS)
The DFS algorithm is a recursive algorithm that uses the idea of backtracking. It involves exhaustive searches of all the nodes by going ahead, if possible, else by backtracking.

![image](https://user-images.githubusercontent.com/43212302/175808416-72fdbc33-274c-478b-bc10-9a7eb2ba3ba7.png)

Screenshot from: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/

### Dijkstra's Algorithm
Dijkstra's Algorithm finds the shortest path between a given node (which is called the "source node") and all other nodes in a graph. This algorithm uses the weights of the edges to find the path that minimizes the total distance (weight) between the source node and all other nodes.

![image](https://user-images.githubusercontent.com/43212302/175808476-75a35b8a-93a7-44ef-90b0-2b69b2adf792.png)

Screenshot from: https://python.plainenglish.io/dijkstras-algorithm-theory-and-python-implementation-c1135402c321

## Output:
The number shows that how many webs did the program search, and also shows the path.

![image](https://user-images.githubusercontent.com/43212302/175808243-4b70d6bd-3292-4698-9d82-85670bdf1a34.png)
