# Relatório da NOME DA ATIVIDADE

**Disciplina: PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA** 

**Aluno(s): Gabriel Yan**

**Turma: SI noturna**

**Professor: Rafael**

**Data: 18/03/2026**

---

# 1. Descrição do Problema

O presente trabalho apresenta a implementação de um sistema para o processamento e soma de uma lista massiva de dados numéricos, composta por 10.000.000 (dez milhões) de números inteiros extraídos de um arquivo de texto (num.txt).O algoritmo utiliza a estratégia de Decomposição de Dados (Data Partitioning), baseada no paradigma de "Dividir e Conquistar". Inicialmente, o programa realiza a leitura integral do arquivo para a memória principal. Em seguida, a lista resultante é segmentada em porções menores (chunks), que são distribuídas equitativamente entre os diversos núcleos de processamento da CPU.O objetivo central da paralelização é otimizar o tempo de resposta do sistema. Em Python, operações de computação intensiva (CPU-bound) enfrentam a limitação do Global Interpreter Lock (GIL), que impede a execução de múltiplas threads em paralelo real. Para superar esse gargalo, utilizou-se a biblioteca multiprocessing, que cria processos independentes com seus próprios interpretadores, permitindo o uso simultâneo de todos os recursos de hardware disponíveis.Em termos de complexidade algorítmica, a soma sequencial é classificada como $O(n)$. Com a implementação paralela, busca-se reduzir o tempo de execução para uma complexidade aproximada de $O(n/p)$, onde $n$ representa a quantidade total de elementos e $p$ o número de processos ou núcleos ativos, desconsiderando-se o overhead de comunicação entre processos.

---

# 2. Ambiente Experimental

Descreva o ambiente em que os experimentos foram realizados.

## Orientações

Informar as características do hardware e software utilizados na execução dos testes.

| Item                        | Descrição |
| --------------------------- | --------- |
| Processador                 |12th Gen Intel(R) Core(TM) i5-12500 (3.00 GHz)|
| Número de núcleos           |    12     |
| Memória RAM                 |   16,0 GB |
| Sistema Operacional         |Windows 11 Pro|
| Linguagem utilizada         |  Python   |
| Biblioteca de paralelização |multiprocessing|
| Compilador / Versão         |Python 3.13.x|

---

# 3. Metodologia de Testes

A avaliação de desempenho do algoritmo foi conduzida de forma empírica, utilizando o tempo de resposta como métrica principal para medir a eficiência da paralelização. O procedimento seguiu as etapas descritas abaixo:

Mensuração do Tempo: O tempo de execução foi calculado utilizando a biblioteca time do Python. A contagem inicia-se imediatamente antes da criação do pool de processos e encerra-se após a consolidação da soma final (reduce), capturando exclusivamente o tempo de processamento paralelo, desconsiderando o tempo de leitura do arquivo em disco (I/O).

Massa de Dados: Foi utilizado um arquivo de entrada (numero2.txt) contendo 10.000.000 (dez milhões) de registros de números inteiros para garantir que a carga de trabalho fosse suficiente para justificar o uso de múltiplos núcleos.

Configurações de Teste: Foram realizados testes incrementais alterando o número de processos ativos para as seguintes configurações: 1 (versão serial), 2, 4, 8 e 12 processos.

Repetições e Média: Para mitigar variações causadas pelo escalonador do Sistema Operacional e por processos em segundo plano, cada configuração foi executada 3 vezes. O valor registrado no relatório corresponde à média aritmética simples dessas execuções.

Condições de Execução: Os testes foram realizados em ambiente controlado, com a máquina em estado de ociosidade, sem outras aplicações de alto consumo de CPU abertas, visando minimizar a contenção de recursos e ruídos nos dados coletados.
---

# 4. Resultados Experimentais

| Nº Threads/Processos | Tempo de Execução (s) |
| -------------------- | --------------------- |
| 1                    |  0.507543             |
| 2                    |  0.397408             |
| 4                    |  0.361267             |
| 8                    |  0.367538             |
| 12                   |  0.341338             |

---

# 5. Cálculo de Speedup e Eficiência

## Fórmulas Utilizadas

### Speedup

```
Speedup(p) = T(1) / T(p)
```

Onde:

* **T(1)** = tempo da execução serial
* **T(p)** = tempo com p threads/processos

### Eficiência

```
Eficiência(p) = Speedup(p) / p
```

Onde:

* **p** = número de threads ou processos

---

# 6. Tabela de Resultados

Preencha a tabela abaixo utilizando os tempos medidos.

| Threads/Processos | Tempo (s) | Speedup | Eficiência |
| ----------------- | --------- | ------- | ---------- |
| 1                 | 0.507543  | 1.0     | 1.0        |
| 2                 | 0.397408  | 1.28    | 0.64       |
| 4                 | 0.361267  | 1.40    | 0.35       |
| 8                 | 0.367538  | 1.38    | 0.17       |
| 12                | 0.341338  | 1.49    | 0.12       |

---

# 7. Gráfico de Tempo de Execução

<img width="750" height="446" alt="image" src="https://github.com/user-attachments/assets/b7aea2b6-2cf7-4c51-9cb4-37c086597918" />


---

# 8. Gráfico de Speedup

<img width="750" height="470" alt="image" src="https://github.com/user-attachments/assets/aff4a43c-d1c9-4004-aae2-010a4e396b1f" />


---

# 9. Gráfico de Eficiência

<img width="750" height="470" alt="image" src="https://github.com/user-attachments/assets/5dc243ea-e041-4f0a-ae31-633a419d16e3" />


---

# 10. Análise dos Resultados

A análise dos dados experimentais revela que a paralelização da soma de 10 milhões de números apresentou um ganho de desempenho real, porém com retornos decrescentes conforme o número de processos aumentou.

Speedup e Escalabilidade: O speedup máximo alcançado foi de 1.49 com 12 processos. Isso indica que, embora o programa tenha rodado mais rápido, ele não atingiu o speedup ideal (que seria 12.0). A escalabilidade foi positiva até 4 núcleos, mas apresentou uma oscilação de desempenho entre 4 e 8 núcleos (onde o tempo subiu de 0.36s para 0.367s), sugerindo que o custo de gerenciamento superou o ganho computacional nesse intervalo.

Eficiência: A eficiência decaiu drasticamente de 1.0 (100%) para 0.12 (12%). Esse comportamento é esperado em algoritmos de baixa complexidade computacional (como a soma), onde o tempo gasto pelo Sistema Operacional para criar processos, copiar a lista de números na memória e coletar os resultados (overhead) é proporcionalmente alto em relação ao tempo da conta matemática em si.

Gargalos e Overhead: O principal gargalo identificado foi a contenção de memória. Somar 10 milhões de números é uma tarefa extremamente rápida para o processador; o tempo medido reflete, em grande parte, a latência de acesso à RAM e o custo de comunicação entre o processo pai e os processos filhos no Windows.

Limites de Hardware: A estabilização dos tempos entre 4 e 12 processos sugere que o hardware atingiu seu limite de largura de banda de memória ou que o número de núcleos físicos da máquina é inferior a 12, fazendo com que processos adicionais disputassem o mesmo recurso físico (Hyper-threading).

---

# 11. Conclusão

O experimento demonstrou com sucesso a aplicação de conceitos de computação concorrente em Python utilizando a biblioteca multiprocessing. Através da estratégia de divisão de carga, foi possível reduzir o tempo de execução da soma de 10 milhões de elementos de 0.507s para 0.341s.

Conclui-se que:

Viabilidade: A paralelização é viável e trouxe um ganho de aproximadamente 32% na velocidade de execução.

Ponto de Equilíbrio: Para este problema específico e nesta máquina, o uso de 4 processos mostrou-se o ponto de maior equilíbrio entre ganho de tempo e eficiência de recursos.
