from pico2d import *


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(1200, 800)
sheet = load_image('sonic-sprite.png')

running = True
while running:
    handle_events()
    clear_canvas()
    sheet.draw(600, 400)
    update_canvas()
    delay(0.05)

close_canvas()
