import pygcurse, pygame, sys
from pygame.locals import *
win = pygcurse.PygcurseWindow(20, 10)
win.colors = ('red', 'gray')
win.autoupdate = False
cellx = 0
celly = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            n_cellx, n_celly = win.getcoordinatesatpixel(event.pos)
            if (n_cellx, n_celly) != (cellx, celly):
                win.setscreencolors(None, 'gray', clear=True)
                win.putchar('@', x=n_cellx, y=n_celly)
                win.update()
                (cellx, celly) = (n_cellx, n_celly)
