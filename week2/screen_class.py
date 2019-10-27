#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)

class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)
    
    def __sub__(self):
        return type(self)(self.x - other.x, self.y - other.y)
    
    def __mul__(self, k):
        self.x *= k
        self.y *= k

    def int_pair(self):
        return (self.x, self.y)
    
    def __len__(self):
        return math.sqrt(self.x**2 + self.y**2)


class Polyline:
    def set_points(self):
        pass
    
    def draw_points(self):
        pass


class Knot(Polyline):
    def get_know(self):
        pass


if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")