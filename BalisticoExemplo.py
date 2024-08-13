from vpython import *
#Web VPython 3.2
esquerda = box(pos=vec(0, 0, 0),length=80, height=1, width=1, color=color.blue)

esfera = sphere(pos=vector(-9,0,0),radius=2,color=color.orange)

while True:
    while True:
        rate(30)
        if esfera.pos.x < 30:  
            esfera.pos.x += 2
            if esfera.pos.x > 0:
                esfera.pos.y -= 2
            elif esfera.pos.x < 0 :
                esfera.pos.y += 2
            elif esfera.pos.x == 0 :
                esfera.pos.y = 50 
        else:
            break 