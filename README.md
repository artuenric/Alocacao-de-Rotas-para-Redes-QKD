# Simulação e Análise de Redes QKD

Este repositório contém um framework em Python e uma série de análises, desenvolvidas em Jupyter Notebooks, para simular e avaliar o desempenho de redes de Distribuição Quântica de Chaves (QKD). O foco principal é a alocação de rotas e o gerenciamento de requisições de chaves quânticas sob diferentes condições.

## Visão Geral do Projeto

O objetivo deste projeto é analisar como diferentes parâmetros da rede QKD afetam seu desempenho. As simulações avaliam métricas como o número de requisições atendidas e o tempo total da simulação, considerando variações em:

* **Capacidade dos canais quânticos.**
* **Número de qubits disponíveis.**
* **Vazão da rede e número de requisições.**
* **Estratégias de alocação de rotas (ex: FIFO).**

## Estrutura do Repositório

* `QKDnet/`: Contém todo o código-fonte da biblioteca de simulação, incluindo as classes para Rede, Controlador, Nós e Canais.
* `Variando a capacidade.ipynb`: Notebook com a análise de desempenho da rede ao variar a capacidade dos canais.
* `Variando o número de qubits.ipynb`: Notebook com a análise de desempenho ao variar a quantidade de qubits nos links.
* `N Requests x Vazão.ipynb`: Notebook focado na análise da vazão da rede em relação ao número de requisições.
* `grafico_*.pdf`: Arquivos PDF gerados pelos notebooks, contendo os gráficos com os resultados das simulações.


## Como Executar as Análises

### 1. Pré-requisitos

Certifique-se de ter Python e as bibliotecas necessárias instaladas. Recomenda-se o uso de um ambiente virtual.

```bash
pip install -r requirements.txt