import pygame
import re
from utils import colors, c_w, button


def draw_board(pygame: pygame, screen: pygame.display) -> None:
    """Draw chess board on the screen

    Args:
        pygame (pygame): main pygame object
        screen (pygame.display): pygame display object
    """
    board = [(x, y)
             for y in range(8) for x in range(8)]
    for i in range(64):
        draw_cell(pygame, screen, board[i])
    return board


def draw_cell(pygame: pygame, screen: pygame.display, p: tuple, player: bool = True, c: str = '') -> None:
    color = get_color((p[0], p[1]), player)
    word = get_word((p[0], p[1]), player)
    font = pygame.font.Font(None, 16)
    cell = font.render(word, True, colors[color])
    if c == '':
        pygame.draw.rect(
            screen, colors['dark' if color == 'light' else 'light'], get_dem(p))
    else:
        pygame.draw.rect(
            screen, colors['highlight'], get_dem(p))
    screen.blit(cell, (c_w * p[0], c_w * p[1]))
    pygame.display.update()


def get_dem(pos: tuple) -> tuple:
    return (c_w * pos[0], c_w * pos[1], c_w, c_w)


def get_color(pos: tuple, player: bool) -> str:
    color = [['light', 'dark'], ['dark', 'light']][player]
    return color[sum(pos) % 2 == 0]


def get_word(pos: tuple, color: bool = True) -> str:
    if pos[0] > 7 or pos[1] > 7:
        return ''
    if color:
        return 'abcdefgh'[pos[0]] + '87654321'[pos[1]]
    else:
        return 'hgfedcba'[pos[0]] + '12345678'[pos[1]]


def get_moves(filename: str) -> list:
    with open(filename, 'r') as f:
        png = f.read()
    return re.findall(r'\d\. ([a-zA-Z0-9-+]* [a-zA-Z0-9-+]*)', re.sub('\n', ' ', png))


def locate_center(rect: pygame.Rect, text: pygame.font) -> tuple:
    x, y = text.get_rect().center
    return rect.center[0] - x, rect.center[1] - y


def draw_button(pg: pygame, screen: pygame.display, base: pygame.Rect, top: pygame.Rect, word: str) -> None:
    font = pygame.font.Font(None, button['fs'])
    text = font.render(word, True, button['font_color'])
    pg.draw.rect(screen, button['base_color'], base, border_radius=button['r'])
    pg.draw.rect(screen, button['top_color'], top, border_radius=button['r'])
    screen.blit(text, locate_center(base, text))
    pygame.display.flip()


'''
Animation from button clicking
base = Rect(50, 60, 200, 100)
top = Rect(50, 60, 200, 90)
elif event.type == MOUSEBUTTONDOWN:
                if top.collidepoint(event.pos):
                    top.move_ip((0, 10))
                    base.update(base.left, base.top + 10,
                    base.width, base.height - 10)
elif event.type == MOUSEBUTTONUP:
    if top.collidepoint(event.pos):
        top.move_ip((0, -10))
        base.update(base.left, base.top - 10,
                    base.width, base.height + 10)
screen.fill(colors['gray'])
draw_button(pygame, screen, base, top, text)
'''

'''
Logic for highlighting chess board cell
elif event.type == MOUSEBUTTONDOWN:
    try:
        x, y = event.pos[0] // c_w, event.pos[1] // c_w
        draw_cell(pygame, screen, (x, y), c='highlight')
    except IndexError:
        pass
elif event.type == MOUSEBUTTONUP:
    try:
        draw_cell(pygame, screen, (x, y))
    except IndexError:
        pass
'''
