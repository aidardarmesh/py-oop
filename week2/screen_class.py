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
    
    def __sub__(self, other):
        return type(self)(self.x - other.x, self.y - other.y)
    
    def __mul__(self, k):
        self.x *= k
        self.y *= k

    def int_pair(self):
        return (self.x, self.y)
    
    def len(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def __str__(self):
        return str(self.int_pair())


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []
    
    def add_point(self, point):
        self.points.append(Vec2d(point))
        self.speeds.append(Vec2d(
            random.random() * 2,
            random.random() * 2
        ))
    
    def get_point(self, alpha, deg=None):
        if deg is None:
            deg = len(self.points) - 1
        if deg == 0:
            return self.points[0]
        return self.points[deg]*alpha + self.get_point(alpha, deg-1)*(1-alpha)
    
    def get_points(self, count):
        alpha = 1/count
        res = []
        for i in range(count):
            res.append(self.get_point(self.points, i*alpha))
        return res
    
    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p] = Vec2d(-self.speeds[p].x, self.speeds[p].y)
            if points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)
    
    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(self.points)-1):
                pygame.draw.line(gameDisplay, color,
                                (int(self.points[p_n].x), int(self.points[p_n].y)),
                                (int(self.points[p_n+1].x), int(self.points[p_n+1].y)), width)

        elif style == "points":
            for p in self.points:
                pygame.draw.circle(gameDisplay, color,
                                (int(p.x), int(p.y)), width)


class Knot(Polyline):
    def get_knot(self):
        pass


if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    pause = True
    knot = Knot()

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    knot = Knot()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                knot.add_point(event.pos)

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        knot.draw_points()
        knot.draw_points(knot.get_knot(), "line", 3, color)
        if not pause:
            knot.set_points()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)