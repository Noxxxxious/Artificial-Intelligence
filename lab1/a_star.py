import queue
import sys
from maze import Maze, path_from


def l1(node1, node2):
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)

def a_star(maze):
    start_node = maze.find_node('S')
    start_node.cost = 0
    q = queue.PriorityQueue(0)
    q.put((start_node.cost, start_node))

    while not q.empty():
        parent = q.get()[1]
        parent.visited = True
        if parent.type == 'E':
            return path_from(parent)

        for child in maze.get_possible_movements(parent):
            new_cost = parent.cost + maze.move_cost(parent, child) + l1(child, maze.find_node('E'))
            if child.cost > new_cost:
                child.cost = new_cost
                child.parent = parent
                q.put((child.cost, child))
    return None


maze = Maze.from_file(sys.argv[1])
maze.draw()
maze.path = a_star(maze)
print()
maze.draw()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end=' ')
print()
