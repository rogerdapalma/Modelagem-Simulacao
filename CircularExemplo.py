from vpython import *
#Web VPython 3.2

from vpython import *


# Configurações da cena
#scene = canvas(width=800, height=600, center=vector(0,0,0))

# Criação dos objetos
esfera = sphere(pos=vector(5, 0, 0), radius=0.5, color=color.cyan, make_trail=True)

box(pos=vec(0, 0, 0),length=1, height=1, width=1, color=color.cyan)

# Parâmetros do movimento circular
raio = 5  # Raio da trajetória circular
velocidade_angular = 2 * pi / 5  # Velocidade angular (rad/s), uma volta a cada 5 segundos

# Tempo inicial
t = 0
dt = 0.01  # Intervalo de tempo

# Loop principal
while True:
    rate(100)
    # Atualiza o tempo
    t += dt
    
    # Calcula a nova posição da esfera
    x = raio * cos(velocidade_angular * t)
    y = raio * sin(velocidade_angular * t)
    
    # Atualiza a posição da esfera
    esfera.pos = vector(x, y, 0)
 
