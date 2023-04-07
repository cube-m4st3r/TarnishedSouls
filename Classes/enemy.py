import random

import db
from Classes.enemy_logic import EnemyLogic


class Enemy:
    def __init__(self, idEnemy):
        result = db.get_enemy_with_id(idEnemy)
        self.id = idEnemy
        self.name = result[0]
        self.logic = EnemyLogic(result[1])
        self.description = result[2]
        self.max_health = result[3]
        self.runes = result[4]
        self.moves = db.get_enemy_moves_with_enemy_id(idEnemy)

        self.health = self.get_max_health()
        self.phase = 0
        self.last_move = None
        self.dodge_next = False

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_logic(self):
        return self.logic

    def get_description(self):
        return self.description

    def get_health(self):
        return self.health

    def get_runes(self):
        return self.runes

    def get_max_health(self):
        return self.max_health

    def get_phase(self):
        return self.phase

    def reduce_health(self, amount):
        self.health = max(self.health - amount, 0)

    def increase_health(self, amount):
        self.health = min(self.health + amount, self.max_health)

    def set_health(self, amount):
        self.health = amount

    def get_move(self, phase):
        available_moves = [move for move in self.moves if move != self.last_move and (move.get_phase() == phase or move.get_phase() == 0)]
        if available_moves:
            selected_move = random.choice(available_moves)
            self.last_move = selected_move
            return selected_move
        else:
            print("Didn't found a valid move anymore!")
            return None

    def dodge(self):
        self.dodge_next = True

    def get_is_dodging(self):
        return self.dodge_next

    def reset_dodge(self):
        self.dodge_next = False

    def increase_phase(self):
        self.phase += 1