import pygame
from pygame.locals import *
from functions import letter_box, cirs_rects, activate
from settings import colors, screen_set, inner, outer, circle_pos, letter_pos
from settings import inner_w


def main():
    # Initialize the game
    pygame.init()
    running = True
    screen = pygame.display.set_mode((screen_set['size']))
    screen.fill(screen_set['background'])
    pygame.draw.rect(screen, colors['white'], outer)
    # pygame.draw.rect(screen, colors['black'], inner, inner_w)
    circles, let_rects = cirs_rects(inner, circle_pos, letter_pos)
    letter_box(pygame, screen, inner, circles, let_rects)
    pygame.display.update()

    activated = []
    chars = 'abcdefghijkl'
    c_sec = ['abc', 'def', 'ghi', 'jkl']
    letters = {str(ord(chars[i])): circles[i] for i in range(12)}
    last = ''
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if activated:
                        removed = activated.pop()
                        activate(pygame, screen, activated[:], removed)
                if str(event.key) in letters:
                    current = letters[str(event.key)]
                    if len(activated) > 0:
                        i = [last in x for x in c_sec].index(True)
                        if chr(event.key) not in c_sec[i]:
                            activated.append(current)
                            activate(pygame, screen, activated[:])
                    else:
                        activated.append(current)
                        activate(pygame, screen, activated[:])
                    last = chr(event.key)
            if event.type == KEYUP:
                if str(event.key) in letters:
                    pass
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
