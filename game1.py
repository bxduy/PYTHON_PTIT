import pygame as pg

WIDTH, HEIGHT = 900, 500
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Game 1')

WHITE = (255, 255, 255)

FPS = 60

def draw_window():
    WIN.fill(WHITE)
    pg.display.update()


def main():
    clock = pg.time.Clock(FPS)
    