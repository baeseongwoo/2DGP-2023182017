import math
from pico2d import *

WIDTH, HEIGHT = 800, 600
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
RADIUS = 200

RECT_POINTS = [(100, 100), (700, 100), (700, 500), (100, 500)]
TRIANGLE_POINTS = [(100, 100), (700, 100), (400, 500)]

running = True


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def draw_frame(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    handle_events()
    delay(0.01)


def move_circle():
    for degree in range(0, 360, 2):
        if not running:
            return
        radian = math.radians(degree)
        x = CENTER_X + RADIUS * math.cos(radian)
        y = CENTER_Y + RADIUS * math.sin(radian)
        draw_frame(x, y)


def move_line(start, end, step=5):
    x1, y1 = start
    x2, y2 = end
    distance = math.hypot(x2 - x1, y2 - y1)
    count = max(1, int(distance / step))
    for i in range(count):
        if not running:
            return
        t = i / count
        draw_frame(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t)


def move_polygon(points):
    for i in range(len(points)):
        if not running:
            return
        move_line(points[i], points[(i + 1) % len(points)])


open_canvas(WIDTH, HEIGHT)
character = load_image('character.png')

while running:
    move_circle()
    move_polygon(RECT_POINTS)
    move_polygon(TRIANGLE_POINTS)

close_canvas()
