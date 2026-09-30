from pico2d import *

# 스프라이트 시트 출처: DS Naruto Shippuden: Ninja Council 4 - Naruto (The Spriters Resource)

CANVAS_W, CANVAS_H = 800, 600

open_canvas(CANVAS_W, CANVAS_H)
sheet = load_image('naruto_sheet.png')

clear_canvas()
sheet.clip_draw(25, 5394, 43, 58, CANVAS_W // 2, CANVAS_H // 2)
update_canvas()
delay(2)

close_canvas()
