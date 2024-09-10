from vpython import *
#Web VPython 3.2

from vpython import *
import random

# Configurações iniciais da cena
scene = canvas(title='Simulação em VPython', width=800, height=600, center=vector(0,0,0), background=color.black)

# Dimensões da caixa (mais longa em X e Y, mais fina em Z)
box_width = 20
box_height = 10
box_depth = 2  # Caixa mais fina no eixo Z

# Criando as paredes da caixa (sem frente e trás)
left_wall = box(pos=vector(-box_width/2, 0, 0), size=vector(0.2, box_height, box_depth), color=color.white)
right_wall = box(pos=vector(box_width/2, 0, 0), size=vector(0.2, box_height, box_depth), color=color.white)
bottom_wall = box(pos=vector(0, -box_height/2, 0), size=vector(box_width, 0.2, box_depth), color=color.white)
top_wall = box(pos=vector(0, box_height/2, 0), size=vector(box_width, 0.2, box_depth), color=color.white)

# Função para gerar uma cor aleatória que não seja branca
def random_color_excluding_white():
    while True:
        color_value = vector(random.random(), random.random(), random.random())
        if color_value != vector(1, 1, 1):  # Evita a cor branca
            return color_value

# Lista para armazenar as bolas rosas
pink_balls = []

# Função para verificar se duas bolas estão colidindo (sobrepostas)
def is_colliding(ball1, ball2):
    return mag(ball1.pos - ball2.pos) < (ball1.radius + ball2.radius)

# Criação das bolas rosas com cores aleatórias diferentes de branco
for i in range(10):
    while True:
        pos_x = random.uniform(-box_width/2 + 1, box_width/2 - 1)
        pos_y = random.uniform(-box_height/2 + 1, box_height/2 - 1)
        pos_z = random.uniform(-box_depth/2 + 1, box_depth/2 - 1)
        new_ball = sphere(pos=vector(pos_x, pos_y, pos_z), radius=0.5, color=random_color_excluding_white())
        new_ball.velocity = vector(0, 0, 0)  # Velocidade inicial zero

        # Verifique se a nova bola não está colidindo com as bolas existentes
        collision = False
        for ball in pink_balls:
            if is_colliding(new_ball, ball):
                collision = True
                break
        
        if not collision:
            pink_balls.append(new_ball)
            break
        else:
            new_ball.visible = False  # Esconde a bola se sobreposta e tenta novamente

# Solicita ao usuário a força inicial da bola branca
force_input = float(input("Digite a força inicial da bola branca (um valor maior que zero): "))

# Criação da bola branca com força inicial personalizada
white_ball = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.white)
white_ball.velocity = vector(force_input, force_input * 1.33, force_input * 0.67)  # Força inicial baseada na entrada do usuário
damping = 0.99  # Fator de dissipação de energia

# Parâmetros de simulação
dt = 0.01

while True:
    rate(100)  # Controla a velocidade da simulação

    # Atualização da posição da bola branca
    white_ball.pos += white_ball.velocity * dt

    # Dissipação da força
    white_ball.velocity *= damping

    # Verificação de colisões com as paredes da caixa para a bola branca
    if white_ball.pos.x + white_ball.radius > box_width/2 or white_ball.pos.x - white_ball.radius < -box_width/2:
        white_ball.velocity.x *= -1  # Inverte a velocidade no eixo x
    if white_ball.pos.y + white_ball.radius > box_height/2 or white_ball.pos.y - white_ball.radius < -box_height/2:
        white_ball.velocity.y *= -1  # Inverte a velocidade no eixo y
    if white_ball.pos.z + white_ball.radius > box_depth/2 or white_ball.pos.z - white_ball.radius < -box_depth/2:
        white_ball.velocity.z *= -1  # Inverte a velocidade no eixo z

    # Verificação de colisões com as bolas rosas
    for ball in pink_balls:
        if is_colliding(white_ball, ball):
            # Calcular nova velocidade após a colisão elástica
            relative_velocity = white_ball.velocity - ball.velocity
            collision_normal = norm(white_ball.pos - ball.pos)
            velocity_along_normal = dot(relative_velocity, collision_normal)
            
            if velocity_along_normal > 0:
                continue

            # Massa das bolas (assumindo massa igual para simplicidade)
            mass_white = 1
            mass_pink = 1

            # Coeficiente de restituição (para colisão elástica)
            e = 1

            # Calcular impulso escalar
            j = -(1 + e) * velocity_along_normal
            j /= (1/mass_white + 1/mass_pink)

            # Calcular vetores de impulso
            impulse = j * collision_normal

            # Atualizar velocidades após a colisão
            white_ball.velocity += impulse / mass_white
            ball.velocity -= impulse / mass_pink

    # Atualizar a posição das bolas rosas
    for i, ball1 in enumerate(pink_balls):
        ball1.pos += ball1.velocity * dt
        ball1.velocity *= damping  # Dissipação de energia para as bolas rosas também

        # Verificação de colisões das bolas rosas com as paredes da caixa
        if ball1.pos.x + ball1.radius > box_width/2 or ball1.pos.x - ball1.radius < -box_width/2:
            ball1.velocity.x *= -1
        if ball1.pos.y + ball1.radius > box_height/2 or ball1.pos.y - ball1.radius < -box_height/2:
            ball1.velocity.y *= -1
        if ball1.pos.z + ball1.radius > box_depth/2 or ball1.pos.z - ball1.radius < -box_depth/2:
            ball1.velocity.z *= -1

        # Verificação de colisões entre bolas rosas
        for j in range(i + 1, len(pink_balls)):
            ball2 = pink_balls[j]
            if is_colliding(ball1, ball2):
                # Calcular nova velocidade após a colisão elástica entre duas bolas rosas
                relative_velocity = ball1.velocity - ball2.velocity
                collision_normal = norm(ball1.pos - ball2.pos)
                velocity_along_normal = dot(relative_velocity, collision_normal)
                
                if velocity_along_normal > 0:
                    continue

                # Calcular impulso escalar
                j = -(1 + e) * velocity_along_normal
                j /= (1/mass_pink + 1/mass_pink)

                # Calcular vetores de impulso
                impulse = j * collision_normal

                # Atualizar velocidades após a colisão
                ball1.velocity += impulse / mass_pink
                ball2.velocity -= impulse / mass_pink
