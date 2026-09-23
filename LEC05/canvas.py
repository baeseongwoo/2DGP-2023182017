## 여기를 채우시오.
from pico2d import *
##form import *안하면 import pico2d 하고 매번 pico2d.open_canvas()이렇게 해야함

open_canvas(800, 600)

character=load_image('character.png')
##character.draw(400,300)
##character.draw(300,200)
##character.draw(500,400)
#---
for x in range(0,9):
    for y in range(0,7):
        character.draw(x*100,y*100)



update_canvas()
delay(10)
update_canvas()

