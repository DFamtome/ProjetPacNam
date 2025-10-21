import pygame
import time

YELLOW = (255, 255, 0)

class PacNam:
    def __init__(self, screen, maze, size):
        self.screen = screen
        self.pc_right_image = pygame.image.load("images/pc_right.png")
        self.pc_left_image = pygame.image.load("images/pc_left.png")
        self.pc_up_image = pygame.image.load("images/pc_up.png")
        self.pc_down_image = pygame.image.load("images/pc_down.png")
        self.last_pos = "r"
        self.size = size
        self.maze = maze
        self.speed = 300
        self.life = 3
        self.dt = 0
        self.pos = self.start_pos()
        self.score = 0
        #fruit pour manger fantôme
        self.power_up = False
        self.timer = 0

    def start_pos(self):
        self.pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        i = int(self.pos.x / self.size)
        j = int((self.pos.y - self.speed * self.dt - self.size / 2) / self.size)
        while (not self.maze.maze[i][j]):
            i = int(self.pos.x / self.size)
            j = int((self.pos.y + self.speed * self.dt + self.size / 2) / self.size)
            self.pos.y += self.size
        while (self.maze.maze[i][j]):
            i = int(self.pos.x / self.size)
            j = int((self.pos.y + self.speed * self.dt + self.size / 2) / self.size)
            self.pos.y += self.size
        self.pos.y -= self.size
        return self.pos

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

    def print(self,direction):
        self.last_pos = direction
        if direction == "r":
            self.screen.blit(self.pc_right_image, (int(self.pos[0] - self.size * 0.45), int(self.pos[1] - self.size * 0.45)))
        elif direction == "l":
            self.screen.blit(self.pc_left_image, (int(self.pos[0] - self.size * 0.45), int(self.pos[1] - self.size * 0.45)))
        elif direction == "u":
            self.screen.blit(self.pc_up_image, (int(self.pos[0] - self.size * 0.45), int(self.pos[1] - self.size * 0.45)))
        elif direction == "d":
            self.screen.blit(self.pc_down_image, (int(self.pos[0] - self.size * 0.45), int(self.pos[1] - self.size * 0.45)))

    def eat(self):
        # TODO
        pass

    def kill(self):
        # TODO
        pass

    def power(self):
        # TODO
        pass

    def action(self, dt):
        self.dt = dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move_up()
            self.print("u")
        if keys[pygame.K_s]  or keys[pygame.K_DOWN]:
            self.move_down()
            self.print("d")
        if keys[pygame.K_a]  or keys[pygame.K_LEFT]:
            self.move_left()
            self.print("l")
        if keys[pygame.K_d]  or keys[pygame.K_RIGHT]:
            self.move_right()
            self.print("r")
        self.print(self.last_pos)
        self.eat()
        self.power()
