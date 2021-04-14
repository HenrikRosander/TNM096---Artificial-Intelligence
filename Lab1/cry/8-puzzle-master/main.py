
import sys

import numpy as np

from astar import AStar
from bfs import BFS
from board import Board
from dfs import DFS
from iddfs import IDDFS


def main():
    p = Board(np.array(eval(sys.argv[2])))
    alg = sys.argv[1]
    if alg == 'bfs':
        s = BFS(p)
    elif alg == 'ids':
        s = IDDFS(p)
    elif alg == 'dfs':
        s = DFS(p)
    elif alg == 'ast':
        s = AStar(p)
    else:
        print("Invalid input, continuing through A*")
        s = AStar(p)
    s.solve()

    file = open(f'{alg}_output1.txt', 'w')

    print('path_to_goal: ' + str(s.path) + '\n')
    print('cost_of_path: ' + str(len(s.path)) + '\n')
    print('nodes_expanded: ' + str(s.nodes_expanded) + '\n')
    print('nodes_explored: ' + str(len(s.explored_nodes)) + '\n')
    print('search_depth: ' + str(s.solution.depth) + '\n')
    print('max_search_depth: ' + str(s.max_depth) + '\n')

    file.close()


if __name__ == "__main__":
    main()
