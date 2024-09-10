from vpython import *
#Web VPython 3.2
from vpython import *

def distancia(corpo1, corpo2):
    # Função para calcular a distância entre dois corpos
    return sqrt(pow(corpo1.pos.x - corpo2.pos.x, 2) + 
                pow(corpo1.pos.y - corpo2.pos.y, 2) + 
                pow(corpo1.pos.z - corpo2.pos.z, 2))

# Define planeta e lua
planeta = sphere(pos=vector(0, 0, 0), radius=1)
lua = sphere(pos=vector(10, 0, 0), make_trail=True, retain=8, radius=0.5)

raio = 10  # Raio orbital
theta = 0  # Ângulo ao redor do eixo z
phi = 0  # Ângulo de inclinação ao redor do eixo y

# Definindo velocidades angulares
omega_theta = 0.05
omega_phi = 0.03
omega_z = 0.02  # Velocidade angular adicional para movimento no eixo z

while True:
    rate(50)
    
    # Atualiza ângulos para movimento circular
    theta += omega_theta
    phi += omega_phi

    # Calcula a nova posição em coordenadas esféricas e converte para coordenadas cartesianas
    x = raio * sin(phi) * cos(theta)
    y = raio * sin(phi) * sin(theta)
    z = raio * cos(phi) + 5 * sin(omega_z * theta)  # Adicionando movimento dinâmico no eixo z

    # Atualiza a posição da lua
    lua.pos = vector(x, y, z)
