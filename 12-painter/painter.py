from p5 import *

# הגדרת קבועים
LIMIT = 1000

# הגדרת משתנים
command = 'r'
godel = 10
color = 'green'
#shapes = []


# אתחול חד-פעמי
def setup():
    size(LIMIT, LIMIT)


def key_pressed():
    global command, godel

    string_key = str(key)

    if string_key == 'c' or string_key == 'r':
        command = string_key
    elif string_key.isnumeric():
        godel = int(string_key) * 10


def mouse_pressed():
    global command, color, godel

    fill(color)

    if command == 'c':
        circle(mouse_x, mouse_y , godel)
    elif command == 'r':
        rect((mouse_x, mouse_y), godel, godel)


# ציור (מחזורי)
def draw():
    global command, godel, color



run()
