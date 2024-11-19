from random import randint, uniform
import time

# Gerar lista de clientes com IDs aleatórios
clientes = [randint(1, 100) for _ in range(10)]

# Simular o tempo de atendimento de cada cliente
for cliente_id in clientes:
    inicio = time.perf_counter()  # Início da medição de tempo

    # Simular atendimento com tempo aleatório entre 0.1 e 1.0 segundos
    time.sleep(uniform(0.1, 1.0))  
    
    fim = time.perf_counter()  # Fim da medição de tempo
    
    tempo_atendimento = fim - inicio  # Tempo total de atendimento
    print(f"Tempo para atender o cliente {cliente_id}: {tempo_atendimento:.8f} segundos")
