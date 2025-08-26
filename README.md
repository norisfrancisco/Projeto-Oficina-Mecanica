# 🔧 Projeto de Modelagem Conceitual – Oficina Mecânica

Este projeto apresenta a modelagem conceitual de um sistema de gerenciamento de ordens de serviço (OS) para uma **oficina mecânica**, com foco em controle de clientes, veículos, equipes, serviços e peças.

## 📘 Descrição do Contexto

Clientes levam veículos à oficina para manutenção ou revisão. Cada veículo é vinculado a uma equipe de mecânicos, que identifica os serviços a serem executados e preenche uma ordem de serviço (OS), contendo a data de emissão, data prevista de conclusão, status e valor total.

A partir da OS, o sistema calcula o custo de cada serviço, baseado em uma tabela de referência de mão-de-obra, e adiciona também o valor das peças utilizadas. O cliente autoriza os serviços, e a mesma equipe é responsável por avaliar e executar os trabalhos.

## 📚 Entidades Modeladas

- **Cliente**: informações de identificação e contato
- **Veículo**: dados do carro vinculado ao cliente
- **Equipe**: responsável pela OS
- **Mecânico**: membros das equipes, com especialidades
- **OS (Ordem de Serviço)**: documento central com data, status e valores
- **Serviço**: ações a serem executadas (mão de obra)
- **Peça**: materiais utilizados
- **Item_Serviço**: serviços inseridos em uma OS
- **Item_Peca**: peças utilizadas em uma OS

## 🔗 Relacionamentos

- Um **cliente** pode ter vários **veículos**
- Um **veículo** pode gerar várias **OS**
- Cada **OS** está vinculada a uma única **equipe**
- Uma **equipe** tem vários **mecânicos**
- Uma **OS** contém vários **serviços** e **peças**
- O valor da **OS** é a soma dos serviços (mão de obra) e peças

## 🛠️ Diagrama Conceitual

![Modelo Oficina](modelos/modelo_oficina.png)

> Caso algum ponto da narrativa não esteja detalhado, utilizei suposições baseadas no funcionamento típico de oficinas, descritas neste README.

---

## 🗂️ Estrutura do Repositório

📦 oficina-mecanica-modelagem
├── README.md
├── modelos/
│ └── modelo_oficina.png
├── scripts/


## 🚀 Submissão

Este projeto foi desenvolvido como parte do desafio da DIO para modelagem conceitual de banco de dados, com foco em normalização e boas práticas de modelagem ER.

