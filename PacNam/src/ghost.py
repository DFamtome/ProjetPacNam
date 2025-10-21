import pygame
import random
import heapq
import math

RED = (255, 0, 0)

        
class Ghost:
    def __init__(self, screen, maze, size, path_ghosts,path_vulnerable_ghosts,pacnam):
        self.screen = screen
        self.pc = pacnam
        self.speed = 200
        self.dt = 0
        self.size = size
        self.maze = maze
        self.path = []
        self.pos = [screen.get_width() / 2, screen.get_height() / 2]
        self.real_pos = (int(self.pos[0] / self.size), int(self.pos[1] / self.size))
        self.ghost_image = pygame.image.load(path_ghosts)
        self.vulnerable_ghost_image = pygame.image.load(path_vulnerable_ghosts)
        
    def move_up(self):
        # TODO
        pass

    def move_down(self):
        # TODO
        pass

    def move_left(self):
        # TODO
        pass

    def move_right(self):
        # TODO
        pass

    def kill(self):
        # TODO
        pass

    def print(self):
        if (self.pc.power_up == False):
            self.screen.blit(self.ghost_image, (int(self.pos[0] - self.size * 0.45), int(self.pos[1] - self.size * 0.45)))
        else:
            self.screen.blit(self.vulnerable_ghost_image, (int(self.pos[0] - self.size * 0.45), int(self.pos[1] - self.size * 0.45)))

    def find_pos(self):
        i = 0
        x = -1
        y = -1
        while (i == 0):
            x = random.randint(0, len(self.maze.maze)-1)
            y = random.randint(0, len(self.maze.maze[0])-1)
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)] :
                x += dx
                y += dy
                if (self.maze.maze[x][y] == 0):
                    return(x, y)
        return (x, y)

    def astar(self, maze, start, end):
        # TODO
        pass

    def action(self, dt):
        self.dt = dt
        self.print()
        # TODO
