import pygame as pg

pg.init()

win = pg.display.set_mode((500, 500))
pg.display.set_caption('First Game')
x = 50
y = 400
height = 60
width = 40
vel = 5

run = True
while run:
    pg.time.delay(50)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and x > vel:
        x -= vel
    if keys[pg.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if keys[pg.K_UP] and y > vel:
        y -= vel
    if keys[pg.K_DOWN] and y < 500 - height - vel:
        y += vel
    win.fill((250, 250, 0))
    pg.draw.rect(win, (255, 50, 50), (x, y, width, height))
    pg.display.update()

pg.quit()