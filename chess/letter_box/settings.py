from asyncio import constants
from pygame import Rect

x, y = 200, 200
w, h = 300, 300
d = 2                 # rectagle_difference_unit
inner = Rect(x, y, w, h)
outer = Rect(x + d, y + d, w - d, h - d)
inner_w = 4
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
        'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "gray": (160, 160, 160),
    "highlight": (204, 183, 174),
    "brown": (153, 76, 0),
    "dark": (112, 162, 163),
    "light": (177, 228, 185)
}

screen_set = {
    "size": (800, 800),
    "background": (160, 160, 160)
}

circle_pos = d
letter_pos = -30
