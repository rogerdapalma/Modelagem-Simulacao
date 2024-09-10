from vpython import *
#Web VPython 3.2
from vpython import *

# Criando as paredes (caixas) à esquerda e à direita
esquerda = box(pos=vec(-10, 0, 0), length=1, height=1, width=1, color=color.blue)
direita = box(pos=vec(10, 0, 0), length=1, height=1, width=1, color=color.red)

# Criando uma esfera (bola) no meio
esfera = sphere(pos=vector(0, 0, 0), radius=1, color=color.orange)

# Definindo as bordas da esfera
bee = esfera.pos.x - esfera.radius  # Borda esquerda da esfera
bde = esfera.pos.x + esfera.radius  # Borda direita da esfera

# Definindo as bordas das paredes (caixas)
bordaDireita = direita.pos.x - (direita.width / 2)  # Borda interna da parede direita
bordaEsquerda = esquerda.pos.x + (esquerda.width / 2)  # Borda interna da parede esquerda

# Definindo a direção inicial da esfera
direcao = 1  # 1 para direita, -1 para esquerda

# Loop de animação
while True:
    rate(30)  # Controla a velocidade da animação

    # Atualiza a posição da esfera
    esfera.pos.x += direcao * 0.1

    # Atualiza as bordas da esfera com a nova posição
    bee = esfera.pos.x - esfera.radius
    bde = esfera.pos.x + esfera.radius

    # Verifica se a esfera colidirá com a parede direita
    if bde >= bordaDireita:
        direcao = -1  # Muda a direção para a esquerda

    # Verifica se a esfera colidirá com a parede esquerda
    if bee <= bordaEsquerda:
        direcao = 1  # Muda a direção para a direita
