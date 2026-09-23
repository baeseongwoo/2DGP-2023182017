from pico2d import*
open_canvas()
character=load_image('character.png')
# grass=load_image('grass.png')

#grass.draw(400,30)
#character.draw(400,90)
#update_canvas()
#delay(10)
#close_canvas()
#--

#x=0
#while x<800:
#    clear_canvas()
#    grass.draw(400,30)
#    character.draw(x,90)
#    update_canvas()
#    x+=2
#    delay(0.01)

# x=200
# y=200

# while True:

#     while x<599:
#         clear_canvas()
#         draw_rectangle(200,400,600,200)
#         character.draw(x,200)
#         update_canvas()
#         x+=1
#         delay(0.001)

#     while y<399:
#         clear_canvas()
#         draw_rectangle(200,400,600,200)
#         character.draw(x,y)
#         update_canvas()
#         y+=1
#         delay(0.001)

#     while x>199:
#         clear_canvas()
#         draw_rectangle(200,400,600,200)
#         character.draw(x,y)
#         update_canvas()
#         x-=1
#         delay(0.001)  

#     while y>199:
#         clear_canvas()
#         draw_rectangle(200,400,600,200)
#         character.draw(x,y)
#         update_canvas()
#         y-=1
#         delay(0.001)


from math import *



thetha=0
while True:
    # radians

    while thetha<91:
        clear_canvas()
        draw_circle(400,300,150)
        character.draw(150*cos(thetha)+400,150*sin(thetha)+300)
        thetha+=1
        update_canvas()
        delay(0.1)
    
    while thetha<181:
            clear_canvas()
            draw_circle(400,300,150)
            character.draw(-150*cos(thetha)+400,150*sin(thetha)+300)
            thetha+=1
            update_canvas()
            delay(0.1)
    
    while thetha<271:
            clear_canvas()
            draw_circle(400,300,150)
            character.draw(-150*cos(thetha)+400,-150*sin(thetha)+300)
            thetha+=1
            update_canvas()
            delay(0.1)
    
    while thetha<361:
            clear_canvas()
            draw_circle(400,300,150)
            character.draw(150*cos(thetha)+400,-150*sin(thetha)+300)
            thetha+=1
            update_canvas()
            delay(0.1)


character.draw(x,y)


update_canvas()
delay(4)