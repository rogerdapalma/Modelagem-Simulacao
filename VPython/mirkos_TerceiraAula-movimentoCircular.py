from vpython import *
#Web VPython 3.2
def distancia(corpo1,corpo2):
    return sqrt(pow(corpo1.pos.x-corpo2.pos.x,2)
    +pow(corpo1.pos.y-corpo2.pos.y,2))
    
def calculaY(raio,coordx):
    return sqrt(pow(raio,2)
    -pow(coordx-10,2))+10
    

planeta = sphere(pos=vector(10,10,0),radius=1)
lua = sphere(pos=vector(10,0,0),
make_trail=True,retain=8,radius=0.5)
i=0
fator=1
raio = distancia(planeta,lua)
while True:#range vai de 0 ate 20
    rate(20)
    lua.pos.x = i
    if fator>0:
        lua.pos.y = calculaY(raio,i)
    else:
        lua.pos.y = 2*raio - calculaY(raio,i)
    i += 1*fator
    if i==2*raio:
        fator=-1
    if i==0:
        fator=1