# DeponiaPidgeonSolver
This project solves the "pidgeon magnetic field" puzzle from the first game of the Deponia series.

This is an example of a starting "configuration":

![Starting configuration](Start.PNG?raw=true "Starting configuration")  

Each "node" as been labeled with a Cartesian coordinate.  
By rotating the active "central nodes" (nodes at the center of circles) we can obtain different configurations.

The target configuration is shown in the following image:

![Target configuration](End.PNG?raw=true "Target configuration")  

Here the smallest pidgeon is in the central house because the central column of the configuration has only one active node.

Given 10 nodes, 6 of them being "active", we can have a total of 210 configurations:  
[Combination](https://en.wikipedia.org/wiki/Combination)

By rotating central nodes (if active) we link each configuration to a maximum of four other configurations.

This can be seen as we are constructing a graph where a vertex is a configuration and an edge links a configuration to another obtained by rotating one of its central nodes.

Once again Dijkstra can help us finding the shortest path from the starting configuration to the target one.

In order to change the starting configuration, one must edit the "start_nodes" variable inside the "solver.py" file.
Here is an example:

```
start_nodes = (
    [node.Node(0, 2, is_center=False, is_active=True),
     node.Node(1, 2, is_center=False, is_active=True),
     node.Node(2, 2, is_center=False, is_active=True),

     node.Node(0, 1, is_center=True, is_active=True),
     node.Node(1, 1, is_center=True, is_active=True),
     node.Node(2, 1, is_center=True, is_active=False),

     node.Node(0, 0, is_center=False, is_active=False),
     node.Node(1, 0, is_center=True, is_active=False),
     node.Node(2, 0, is_center=False, is_active=True),
```

Here is a possible output:
```
Rotations to apply
((1, 1) - (c: True, a: True))
((1, 1) - (c: True, a: True))
((1, 1) - (c: True, a: True))
((1, 0) - (c: True, a: True))
((0, 1) - (c: True, a: True))
((1, 0) - (c: True, a: True))
((1, 0) - (c: True, a: True))
((0, 1) - (c: True, a: True))
((1, 0) - (c: True, a: True))
```

