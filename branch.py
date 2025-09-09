import pygame

class Branch:
    def __init__(self, parent, pos, dir):
        self.pos = pos
        self.parent = parent
        self.dir = dir
        self.og_dir = dir
        self.count = 0

    def reset(self):
        self.dir = self.og_dir
        self.count = 0
