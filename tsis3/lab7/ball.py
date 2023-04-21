import pygame as pg
import sys
pg.init()
screen = pg.display.set_mode((800,800))
x = y = 400
clock = pg.time.Clock()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            pg.quit()
            sys.exit()

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        y -= 5
    if keys[pg.K_a]:
        x -= 5
    if keys[pg.K_s]:
        y += 5
    if keys[pg.K_d]:
        x += 5

    if x > 775:
        x = 775
    if x < 25:
        x = 25
    if y > 775:
        y = 775
    if y < 25:
        y = 25
    screen.fill('white')
    pg.draw.circle(surface = screen, color = (255,0,0), center = (x,y), radius = 25)
    pg.display.flip()
    clock.tick(60)