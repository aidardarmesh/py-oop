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

    def __add__(self):
        pass
    
    def __sub__(self):
        pass
    
    def __mul__(self):
        pass

    def int_pair(self):
        pass
    
    def len(self):
        pass


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

