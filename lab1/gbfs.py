import sys
import queue
from maze import Maze, path_from


def l1(node1, node2):
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)

def gbfs(maze):
    start_node = maze.find_node('S')
    start_node.cost = 0
    q = queue.PriorityQueue(0)
    q.put((start_node.cost, start_node))
    while not q.empty():
        node = q.get()[1]
        node.visited = True
        if node.type == 'E':
            return path_from(node)

        children = maze.get_possible_movements(node)
        for child in children:
            if not child.visited:
                child.parent = node
                q.put((l1(child, maze.find_node('E')), child))

    return None


maze = Maze.from_file(sys.argv[1])
maze.draw()
maze.path = gbfs(maze)
print()
maze.draw()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end=' ')
print()
