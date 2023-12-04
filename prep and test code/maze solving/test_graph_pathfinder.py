from maze_graph import Graph, Directions

## TEST CODE
g = Graph()
n1 = g.start
n2 = g.add_node(n1, Directions.UP)
n3 = g.add_node(n2, Directions.LEFT)
n4 = g.add_node(n3, Directions.DOWN)
n5 = g.add_node(n2, Directions.UP)
n6 = g.add_node(n5, Directions.LEFT)
n7 = g.add_node(n6, Directions.UP)
n8 = g.add_node(n7, Directions.RIGHT)
n9 = g.add_node(n8, Directions.RIGHT)
n10 = g.add_node(n9, Directions.RIGHT)
n11 = g.add_node(n9, Directions.DOWN)
n12 = g.add_node(n11, Directions.DOWN)
n13 = g.add_node(n12, Directions.RIGHT)
n14 = g.add_node(n10, Directions.DOWN)
n15 = g.add_node(n12, Directions.DOWN)
n16 = g.add_node(n15, Directions.RIGHT)

print(g.pathfind(n1, n14))

print(g.get_xy_coordinates())
print(g.get_xy_coordinates(n10))
print(g.get_xy_coordinates(n7))