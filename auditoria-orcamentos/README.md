# 🏢 Auditoria de Orçamentos Corporativos (Python)
 
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-concluído-brightgreen.svg)]()
 
## 📖 Sobre o Projeto
Este projeto foi desenvolvido como parte da disciplina de Prototipagem de Sistemas Computacionais do curso de Tecnologia da Informação. O objetivo do script é processar e calcular o orçamento de uma estrutura organizacional em formato de dicionário aninhado, simulando departamentos e subdepartamentos de uma empresa.

A solução utiliza conceitos de Python como recursão, decorators, `*args` e `**kwargs`, permitindo calcular o orçamento total, ignorar setores específicos e aplicar uma taxa de conversão no resultado final.
 
## 🚀 Funcionalidades
- **Cálculo Hierárquico:** Varredura da estrutura corporativa, mesmo com vários níveis de profundidade.
- **Filtros Dinâmicos:** Permite ignorar setores específicos e seus subsetores no cálculo.
- **Conversão de Câmbio:** Suporte a taxa de câmbio informada por parâmetro.
- **Sistema de Auditoria:** Exibe informações da execução, como argumentos utilizados e tempo de processamento.
 
## 🛠️ Tecnologias e Conceitos Aplicados
Este projeto foi construído utilizando Python puro, com foco nos seguintes recursos:

* **Funções Recursivas:** utilizadas para navegar pelos dicionários aninhados.
* **Decorators:** implementação do `@auditor` para mostrar dados da execução sem alterar a lógica principal.
* **`*args` e `**kwargs`:** usados para receber departamentos ignorados e parâmetros opcionais, como moeda e taxa de câmbio.
 
## ⚙️ Como Executar
 
### Pré-requisitos
* Python 3.8 ou superior instalado.
 
### Passo a Passo
1. Clone este repositório:
   ```bash
   git clone https://github.com/SeuUsuario/seu-repositorio.git
   A função calcular_orcamento percorre o dicionário da empresa usando recursão. Quando encontra outro dicionário, ela chama a si mesma novamente para continuar entrando nos subdepartamentos. Quando encontra um valor numérico, soma esse valor ao total.

O decorator @auditor foi usado para mostrar o início da auditoria, os parâmetros passados na função e o tempo que o programa levou para executar. Assim, o código fica mais organizado e a parte de auditoria fica separada da lógica do cálculo.

Dados: Os dados simulados da empresa foram estruturados em um dicionário chamado empresa_data, começando pela Matriz e dividindo os setores em TI, RH e Financeiro. Alguns setores possuem subdepartamentos, como Infraestrutura, Desenvolvimento e Cultura, e os últimos níveis possuem os valores dos orçamentos.
Autor
Vinicius Xavier]
E-mail: [xvini096@gmail.com]
