import pygame
import math


class Target:
    MAX_SIZE = 30
    GROWTH = 0.2
    COLOR = 'red'
    INNER_COLOR = 'white'

    def __init__(self, x, y) -> None:
        self.x_coord = x
        self.y_coord = y
        self.size = 0
        self.grow = True

    def update(self):
        if self.size + self.GROWTH >= self.MAX_SIZE:
            self.grow = False
        
        if self.grow:
            self.size += self.GROWTH
        else:
            self.size -= self.GROWTH
    
    def draw_target(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x_coord, self.y_coord), self.size)
        pygame.draw.circle(win, self.INNER_COLOR, (self.x_coord, self.y_coord), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR, (self.x_coord, self.y_coord), self.size * 0.6)
        pygame.draw.circle(win, self.INNER_COLOR, (self.x_coord, self.y_coord), self.size * 0.4)
                           
    def collide(self, x, y):
        distance = math.sqrt((x - self.x_coord) ** 2 + (y - self.y_coord) ** 2)
        return distance <= self.size
