import pygame

class Leaf:
    def __init__(self, pos):
        self.pos = pos
        self.reached = False
        self.closest_branch = None
