import pygame
from settings import colors, alpha
from math import atan2, cos, sin


def letter_box(pygame, screen, rect, circles, rects) -> None:
    pygame.draw.rect(screen, colors['black'], rect, 4)
    for point in circles:
        draw_circles(pygame, screen, 'black', 'white', point)

    font = pygame.font.Font(None, 45)
    cells = [font.render(x, True, colors['white']) for x in 'ABCDEFGHIJKL']
    cell_rects = [cells[i].get_rect(center=(rects[i][0], rects[i][1]))
                  for i in range(12)]
    for i in range(12):
        screen.blit(cells[i], cell_rects[i])


def draw_circles(pygame, screen, c1, c2, pos) -> None:
    pygame.draw.circle(screen, colors[c1], pos, 14)
    pygame.draw.circle(screen, colors[c2], pos, 10)


def points(rect: pygame.Rect, unit: int) -> list:
    arr = []
    def ms(a, b): return [((b[0] - a[0]) // 2 + a[0], (b[1] - a[1]) // 2 + a[1]),
                          b, ((b[0] - a[0]) // 2 + b[0], (b[1] - a[1]) // 2 + b[1])]

    def ps(a, x, y): return [(b[0] + x, b[1] + y) for b in a]
    arr.extend(ps(ms(rect.topleft, rect.midtop), 0, unit))
    arr.extend(ps(ms(rect.bottomright, rect.midright), -unit, 0))
    arr.extend(ps(ms(rect.bottomleft, rect.midbottom), 0, -unit))
    arr.extend(ps(ms(rect.bottomleft, rect.midleft), unit, 0))
    return arr


def cirs_rects(rect: pygame.Rect, c_unit: int, r_unit: int) -> list:
    return [points(rect, c_unit), points(rect, r_unit)]


def gen_chars() -> str:
    return 'abcdefghijkl'


def activate(pygame, screen, clicked: list, remove: tuple = ()) -> None:
    if remove:
        draw_circles(pygame, screen, 'black', 'white', remove)
        if len(clicked) > 0:
            line = surface_location(clicked[-1], remove, 14)
            pygame.draw.line(screen, colors['white'], line[0], line[1], 2)
    if not clicked:
        return

    temp = pos_to_surface_pos(clicked)
    if len(temp) > 0:
        for line in temp:
            pygame.draw.lines(screen, colors['black'], False, line, 2)

    active = clicked.pop()
    draw_circles(pygame, screen, 'highlight', 'black', active)

    for point in clicked:
        draw_circles(pygame, screen, 'highlight', 'white', point)


def pos_to_surface_pos(pos: list) -> list:
    if len(pos) < 2:
        return []
    p1 = pos[0]
    temp = []
    for p2 in pos[1:]:
        temp.append(surface_location(p1, p2, 14))
        p1 = p2
    return temp


def surface_location(p1, p2, r) -> tuple:
    temp = surface_location_helper(p1, p2, r)
    new_p1 = p1[0] + temp[0], p1[1] + temp[1]
    temp = surface_location_helper(p2, p1, r)
    new_p2 = p2[0] + temp[0], p2[1] + temp[1]
    return new_p1, new_p2


def surface_location_helper(p1, p2, r) -> tuple:
    deg = atan2(p2[1] - p1[1], p2[0] - p1[0])
    while deg < 0.0:
        deg += 3.1415 * 2
    x = r * cos(deg)
    y = r * sin(deg)
    return x, y
