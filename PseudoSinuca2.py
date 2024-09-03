from vpython import *
#Web VPython 3.2

from vpython import *
import random

# Configurações iniciais da cena
scene = canvas(title='Simulação em VPython', width=800, height=600, center=vector(0, 0, 0), background=color.black)

# Dimensões da caixa
box_width = 20
box_height = 10
box_depth = 2

# Criando as paredes da caixa
left_wall = box(pos=vector(-box_width/2, 0, 0), size=vector(0.2, box_height, box_depth), color=color.white)
right_wall = box(pos=vector(box_width/2, 0, 0), size=vector(0.2, box_height, box_depth), color=color.white)
bottom_wall = box(pos=vector(0, -box_height/2, 0), size=vector(box_width, 0.2, box_depth), color=color.white)
top_wall = box(pos=vector(0, box_height/2, 0), size=vector(box_width, 0.2, box_depth), color=color.white)

def random_color_excluding_white():
    while True:
        color_value = vector(random.random(), random.random(), random.random())
        if color_value != vector(1, 1, 1):
            return color_value

pink_balls = []

def is_colliding(ball1, ball2):
    return mag(ball1.pos - ball2.pos) < (ball1.radius + ball2.radius)

def all_balls_stopped(threshold=0.01):
    if mag(white_ball.velocity) > threshold:
        return False
    for ball in pink_balls:
        if mag(ball.velocity) > threshold:
            return False
    return True

# Criação das bolas rosas
for i in range(10):
    while True:
        pos_x = random.uniform(-box_width/2 + 1, box_width/2 - 1)
        pos_y = random.uniform(-box_height/2 + 1, box_height/2 - 1)
        pos_z = 0
        new_ball = sphere(pos=vector(pos_x, pos_y, pos_z), radius=0.5, color=random_color_excluding_white())
        new_ball.velocity = vector(0, 0, 0)

        collision = False
        for ball in pink_balls:
            if is_colliding(new_ball, ball):
                collision = True
                break
        
        if not collision:
            pink_balls.append(new_ball)
            break
        else:
            new_ball.visible = False

# Criação da bola branca
white_ball = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.white)
white_ball.velocity = vector(0, 0, 0)
damping = 0.99
dt = 0.01

# Loop principal da simulação
while True:
    force_input = float(input("Digite a força inicial da bola branca (um valor maior que zero): "))
    white_ball.velocity = vector(force_input, force_input * 1.33, 0)

    jogada_em_andamento = True

    while jogada_em_andamento:
        rate(100)

        white_ball.pos += white_ball.velocity * dt
        white_ball.velocity *= damping

        if white_ball.pos.x + white_ball.radius > box_width/2 or white_ball.pos.x - white_ball.radius < -box_width/2:
            white_ball.velocity.x *= -1
        if white_ball.pos.y + white_ball.radius > box_height/2 or white_ball.pos.y - white_ball.radius < -box_height/2:
            white_ball.velocity.y *= -1

        for ball in pink_balls:
            if is_colliding(white_ball, ball):
                relative_velocity = white_ball.velocity - ball.velocity
                collision_normal = norm(white_ball.pos - ball.pos)
                velocity_along_normal = dot(relative_velocity, collision_normal)
                
                if velocity_along_normal > 0:
                    continue

                mass_white = 1
                mass_pink = 1
                e = 1

                j = -(1 + e) * velocity_along_normal
                j /= (1/mass_white + 1/mass_pink)

                impulse = j * collision_normal

                white_ball.velocity += impulse / mass_white
                ball.velocity -= impulse / mass_pink

        for i, ball1 in enumerate(pink_balls):
            ball1.pos += ball1.velocity * dt
            ball1.velocity *= damping

            if ball1.pos.x + ball1.radius > box_width/2 or ball1.pos.x - ball1.radius < -box_width/2:
                ball1.velocity.x *= -1
            if ball1.pos.y + ball1.radius > box_height/2 or ball1.pos.y - ball1.radius < -box_height/2:
                ball1.velocity.y *= -1

            for j in range(i + 1, len(pink_balls)):
                ball2 = pink_balls[j]
                if is_colliding(ball1, ball2):
                    relative_velocity = ball1.velocity - ball2.velocity
                    collision_normal = norm(ball1.pos - ball2.pos)
                    velocity_along_normal = dot(relative_velocity, collision_normal)
                    
                    if velocity_along_normal > 0:
                        continue

                    j = -(1 + e) * velocity_along_normal
                    j /= (1/mass_pink + 1/mass_pink)

                    impulse = j * collision_normal

                    ball1.velocity += impulse / mass_pink
                    ball2.velocity -= impulse / mass_pink

        if all_balls_stopped():
            jogada_em_andamento = False
            print("Todas as bolas pararam. Prepare-se para a próxima jogada.")
