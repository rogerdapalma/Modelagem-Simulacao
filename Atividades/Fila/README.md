# Teoria das Filas

Na **teoria das filas**, sistemas de atendimento são estudados com base na ordem de chegada e no processamento dos clientes. Esses sistemas modelam diversos cenários reais, como atendimento em bancos, hospitais, ou call centers.

## Modelos Comuns de Filas

Os sistemas de filas seguem diferentes regras para determinar a ordem de atendimento dos clientes. Os modelos mais comuns são:

- **FIFO (First In, First Out)**: O primeiro cliente a chegar é o primeiro a ser atendido.
- **LIFO (Last In, First Out)**: O último cliente a entrar na fila é o primeiro a ser atendido.
- **SIRO (Serviço em Ordem Aleatória)**: O próximo cliente a ser atendido é escolhido aleatoriamente.
- **Prioridade**: Clientes são atendidos com base em uma prioridade estabelecida (ex.: emergências médicas).

## Componentes de um Sistema de Fila

Um sistema de fila geralmente é composto pelos seguintes elementos:

- **Cliente**: Entidade que solicita um serviço. Pode ser uma pessoa, uma máquina ou um pacote de dados.
- **Servidor**: Entidade que atende o cliente. Pode ser um atendente humano, uma máquina ou um sistema automatizado.
- **Serviço**: Processo ou ação que o servidor realiza para atender o cliente.
- **Fila**: Local (físico ou lógico) onde os clientes aguardam para serem atendidos.

### Condições para Operação

- **Número mínimo de clientes**: Para que a fila funcione, deve haver ao menos 1 cliente.
- **Capacidade do servidor**: Determina a **velocidade de atendimento**, que impacta diretamente no tempo de espera.

## Exemplo Prático: Fila do Cinema

No contexto de uma fila em um cinema:

- **Clientes**: Pessoas que chegam ao cinema para assistir a um filme.
- **Serviço**: Exibição do filme e/ou venda de ingressos.
- **Servidores**: 
  - Caixa que realiza a venda dos ingressos.
  - O sistema de projeção que exibe o filme.

### Dinâmica do Sistema

1. **Entrada na Fila**: Clientes chegam e se posicionam na fila.
2. **Atendimento**: O servidor (caixa) atende os clientes conforme a ordem da fila.
3. **Consumação do Serviço**: Após a compra do ingresso, os clientes assistem ao filme.

### Fatores Críticos

- **Taxa de chegada**: Quantos clientes chegam por unidade de tempo.
- **Taxa de atendimento**: Quantos clientes o servidor consegue atender por unidade de tempo.

## Benefícios do Estudo da Teoria das Filas

- **Otimização**: Permite reduzir o tempo de espera e aumentar a eficiência do atendimento.
- **Planejamento**: Ajuda no dimensionamento de recursos, como número de atendentes necessários.
- **Aplicações Práticas**: Usado em diversos setores como saúde, transportes, tecnologia, e serviços.

--- 
