# 🚚 Logística: Sistema de Priorização de Entregas
 
## 📝 Descrição do Projeto
Este projeto consiste em um algoritmo de suporte à decisão logística focado na otimização de rotas e priorização de entregas. O objetivo principal é calcular o tempo estimado de chegada (ETA) e definir a urgência de cada serviço com base em variáveis externas, como o estado do trânsito e horários limite.
 
O sistema processa dados de entrada (endereço, horário limite e densidade do trânsito) para organizar uma lista de entregas eficiente, garantindo que pacotes críticos sejam marcados com "Prioridade Alta" sempre que o tempo estimado ultrapassar a janela de entrega permitida.
 

*Figura 1: Fluxo lógico do processamento de entregas e tomada de decisão.*
 
## 🚀 Lógica do Algoritmo
O sistema opera através de três decisões sequenciais fundamentais:
* **Decisão 1 (Ajuste de Trânsito):** Se o trânsito for classificado como "Pesado", o tempo estimado de entrega recebe um acréscimo de 20 minutos.
* **Decisão 2 (Verificação de Urgência):** Se o Tempo Estimado > Horário Limite, a entrega é sinalizada como "Urgente" (`Verdadeiro`).
* **Decisão 3 (Definição de Prioridade):** Entregas urgentes recebem status de "Prioridade Alta"; as demais seguem como "Prioridade Normal".
 
## 📊 Tecnologias e Conceitos Utilizados
* **Linguagem:** Pseudocódigo (Portugol) para modelagem lógica.
* **Estruturas de Controle:** Condicionais aninhadas (`SE/ENTÃO/SENÃO`) e operadores lógicos.
* **Testes de Mesa:** Validação de cenários reais, incluindo fluxos de sucesso e tratamento de valores inválidos (ex: trânsito "muito ruim").
 
## 🔧 Resultados e Aprendizados
O desenvolvimento deste projeto permitiu simular diferentes cenários operacionais:
* **Cenário A (Normal):** Trânsito médio e horário dentro do limite resultam em prioridade normal.
* **Cenário B (Limite):** Trânsito pesado elevando o tempo total (ex: 30 + 20 = 50 min), disparando o alerta de urgência.
* **Tratamento de Erros:** Identificação de que o sistema precisa de validações de dados mais robustas para lidar com entradas não previstas.
 
## 🧠 Reflexão Crítica
* **O Maior Desafio:** Transformar um problema real e complexo (trânsito e logística) em decisões binárias simples de `Sim/Não`. A realidade possui muitas variações que o algoritmo precisa simplificar em regras fixas.
* **Melhoria Contínua:** A adição de uma camada de validação de dados é o próximo passo para tornar o sistema mais seguro e confiável contra falhas de entrada.
 
---

[Voltar ao início](https://github.com/ViniciusXS38/portfolio-vinicius-xavier-da-silva)
