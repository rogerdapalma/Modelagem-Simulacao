from vpython import *
#Web VPython 3.2
esquerda = box(pos=vec(-10, 0, 0),length=1, height=1, width=1, color=color.blue)

direita = box(pos=vec(10, 0, 0),length=1, height=1, width=1, color=color.red)
#esfera no meio
esfera = sphere(pos=vector(0,0,0),radius=1,color=color.orange)
#criando movimento para direita

while True:
    rate(5)
    if esfera.pos.x < direita.pos.x - 2:  # Ajuste 1 para parar antes do cubo
        esfera.pos.x += 1
    else:
        break  # Para o movimento quando a esfera alcançar o limite
# tafera para proxima aula, fazer que a esfera bata no quadrado direito e va para o quadrado esquerdo