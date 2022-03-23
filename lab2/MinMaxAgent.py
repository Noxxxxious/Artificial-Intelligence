import random
import math
import copy
from exceptions import AgentException


class MinMaxAgent:
    def __init__(self, my_token='o'):
        self.my_token = my_token

    def decide(self, connect4):
        if connect4.who_moves != self.my_token:
            raise AgentException('not my round')
        return self.minmax(connect4)[1]

    def minmax(self, connect4, depth=5, maximizing=True, alfa=-math.inf, beta=math.inf):
        if self.my_token == 'o':
            enemy = 'x'
        else:
            enemy = 'o'
        if connect4.check_game_over():
            if connect4.wins == self.my_token:
                return 10000, None
            if connect4.wins == enemy:
                return -10000, None
            return 0, None
        if depth == 0:
            score = 0
            score += 3 * connect4.center_column().count(self.my_token)
            scores = connect4.iter_fours()
            for sc in scores:
                a = sc.count(self.my_token)
                b = sc.count(enemy)
                if a == 2:
                    score += 2
                elif a == 3:
                    score += 5
                if b == 3:
                    score -= 4
            return [score, None]
        if maximizing:
            best_result = -math.inf
            best_move = None
            for move in connect4.possible_drops():
                connect4_copy = copy.deepcopy(connect4)
                connect4_copy.drop_token(move)
                result = self.minmax(connect4_copy, depth - 1, False)
                if result[0] > best_result:
                    best_result = result[0]
                    best_move = move
                alfa = max(alfa, best_result)
                if alfa >= beta:
                    break
            return best_result, best_move
        else:
            best_result = math.inf
            best_move = None
            for move in connect4.possible_drops():
                connect4_copy = copy.deepcopy(connect4)
                connect4_copy.drop_token(move)
                result = self.minmax(connect4_copy, depth - 1, True)
                if result[0] < best_result:
                    best_result = result[0]
                    best_move = move
                beta = min(beta, best_result)
                if alfa >= beta:
                    break
            return best_result, best_move
