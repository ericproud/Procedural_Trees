import math
import pygame
from config import *
from branch import *
from leaf import *
from random import randint

class Tree:
    def __init__(self):
        self.branches = []
        self.leaves = []
        self.fully_grown = False
        self.build_crown_rect()
        print("CROWN")
        self.build_trunk()
        print("TRUNK")

    def build_crown_rect(self):
        min_x = (SCREEN_WIDTH // 2) - TREE_WIDTH
        max_x = (SCREEN_WIDTH // 2) + TREE_WIDTH
        min_y = SCREEN_HEIGHT - TRUNK_HEIGHT - TREE_HEIGHT
        max_y = SCREEN_HEIGHT - TRUNK_HEIGHT

        for i in range(LEAF_COUNT):
            pos = pygame.math.Vector2(randint(min_x, max_x), randint(min_y, max_y))
            self.leaves.append(Leaf(pos.copy()))



    def build_trunk(self):
        pos = pygame.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT)
        dir = pygame.math.Vector2(0, -1)
        root = Branch(None, pos.copy(), dir)
        self.branches.append(root)

        pos -= pygame.math.Vector2(0, BRANCH_LEN)
        curr = Branch(root, pos.copy(), dir)
        self.branches.append(curr)

        while root.pos.y - curr.pos.y < TRUNK_HEIGHT:
            print("HI")
            print(root.pos.y - curr.pos.y)
            pos -= pygame.math.Vector2(0, BRANCH_LEN)
            trunk = Branch(root, pos.copy(), dir)
            self.branches.append(trunk)
            curr = trunk
        print("DONE")

    def grow(self):
        if self.fully_grown:
            return
        
        if (len(self.leaves) == 0):
            self.fully_grown = True
            return
        
        branches_count = len(self.branches)
        
        i = 0
        while i < len(self.leaves):
            leaf = self.leaves[i]
            leaf_reached = False
            leaf.closest_branch = None
            dir = pygame.math.Vector2(0,0)

            for j in range(len(self.branches)):
                branch = self.branches[j]

                dir = leaf.pos - branch.pos
                dist = dir.copy().length()
                dir = dir.normalize()

                if dist <= MIN_DIST:
                    del self.leaves[i]
                    leaf_reached = True

                elif dist <= MAX_DIST:
                    if leaf.closest_branch is None:
                        leaf.closest_branch = branch
                    elif (leaf.pos - leaf.closest_branch.pos).length_squared() > dist**2:
                        leaf.closest_branch = branch

            if not leaf_reached:
                if leaf.closest_branch is not None:
                    dir = leaf.pos - leaf.closest_branch.pos
                    dist = dir.copy().length()
                    dir = dir.normalize()
                    leaf.closest_branch.dir = leaf.closest_branch.dir + dir
                    leaf.closest_branch.count += 1

                i+= 1

        for branch in self.branches:
           if branch.count > 0:
                avg_dir = (branch.dir / branch.count).normalize()

                child_pos = branch.pos + avg_dir * BRANCH_LEN
                child_branch = Branch(branch, child_pos, avg_dir)

                self.branches.append(child_branch)
                branch.reset()

        if len(self.branches) == branches_count:
            self.fully_grown = True

    def draw(self, screen):
        for branch in self.branches:
            print()
            
            if branch.parent is None:
                pygame.draw.line(screen, (255,255,255), branch.pos, (SCREEN_WIDTH/ 2, SCREEN_HEIGHT), 3)
            else:
                pygame.draw.line(screen, (255,255,255), branch.pos, branch.parent.pos, 3)

        for leaf in self.leaves:
            pygame.draw.circle(screen, (0,0,0), leaf.pos, 2)


