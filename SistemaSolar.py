from vpython import *
#Web VPython 3.2
from vpython import *
import random 

# Configurações da cena
scene = canvas(width=800, height=600, center=vector(0, 0, 0), background=color.black)

# Função para criar estrelas no fundo
def criar_estrelas(quantidade):
    for _ in range(quantidade):
        # Posição aleatória para cada estrela
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        z = random.uniform(-10, 10)
        
        # Criar a estrela como uma pequena esfera branca
        sphere(pos=vector(x, y, z), radius=0.01, color=color.white)

# Criar estrelas
criar_estrelas(200)  # Número de estrelas a ser criado

# Criar o Sol
sol = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.yellow)

# Função para criar planetas
def criar_planeta(posicao_inicial, raio, cor, velocidade_orbital, velocidade_rotacao):
    planeta = sphere(pos=posicao_inicial, radius=raio, color=cor, make_trail=True)
    planeta.velocidade_orbital = velocidade_orbital
    planeta.velocidade_rotacao = velocidade_rotacao
    planeta.eixo = vector(0, 1, 0)  # Eixo de rotação
    return planeta

# Criação dos planetas
mercurio = criar_planeta(vector(0.7, 0, 0), 0.05, color.gray(0.5), 0.03, 0.1)
venus = criar_planeta(vector(1, 0, 0), 0.08, color.orange, 0.02, 0.08)
terra = criar_planeta(vector(1.5, 0, 0), 0.1, color.blue, 0.01, 0.05)
marte = criar_planeta(vector(2, 0, 0), 0.09, color.red, 0.008, 0.04)
jupiter = criar_planeta(vector(3.5, 0, 0), 0.2, color.orange, 0.005, 0.02)
saturno = criar_planeta(vector(5, 0, 0), 0.15, color.yellow, 0.003, 0.015)

# Tempo inicial
t = 0
dt = 0.01  # Intervalo de tempo

# Loop principal
while True:
    rate(1000)
    t += dt
    
    # Movimento de Mercúrio
    mercurio.pos = vector(0.7 * cos(mercurio.velocidade_orbital * t), 0.7 * sin(mercurio.velocidade_orbital * t), 0)
    mercurio.rotate(angle=mercurio.velocidade_rotacao * dt, axis=mercurio.eixo)
    
    # Movimento de Vênus
    venus.pos = vector(1 * cos(venus.velocidade_orbital * t), 1 * sin(venus.velocidade_orbital * t), 0)
    venus.rotate(angle=venus.velocidade_rotacao * dt, axis=venus.eixo)
    
    # Movimento da Terra
    terra.pos = vector(1.5 * cos(terra.velocidade_orbital * t), 1.5 * sin(terra.velocidade_orbital * t), 0)
    terra.rotate(angle=terra.velocidade_rotacao * dt, axis=terra.eixo)
    
    # Movimento de Marte
    marte.pos = vector(2 * cos(marte.velocidade_orbital * t), 2 * sin(marte.velocidade_orbital * t), 0)
    marte.rotate(angle=marte.velocidade_rotacao * dt, axis=marte.eixo)
    
    # Movimento de Júpiter
    jupiter.pos = vector(3.5 * cos(jupiter.velocidade_orbital * t), 3.5 * sin(jupiter.velocidade_orbital * t), 0)
    jupiter.rotate(angle=jupiter.velocidade_rotacao * dt, axis=jupiter.eixo)
    
    # Movimento de Saturno
    saturno.pos = vector(5 * cos(saturno.velocidade_orbital * t), 5 * sin(saturno.velocidade_orbital * t), 0)
    saturno.rotate(angle=saturno.velocidade_rotacao * dt, axis=saturno.eixo)
