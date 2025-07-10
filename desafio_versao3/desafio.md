# Projeto Desafio DIO.ME  
## Criando um Sistema Bancário com Python

### 🧩 Versão 1: Regras Básicas

O desafio proposto consistia na criação de um sistema bancário simples para um único usuário, respeitando quatro regras principais:

- Não permitir **depósitos** ou **saques** com **valores negativos**;
- Limitar **saques** a um valor máximo de **R$ 500** por operação;
- Restringir o número de **saques** e **depósitos** a **5 por dia**;
- Registrar todas as movimentações em um **extrato**, acessível mediante solicitação do usuário.

---

### 🪛 Versão 2: Evolução em limites trasações

O desafio proposto consistia na criação de um sistema bancário simples para um único usuário, respeitando quatro regras principais:

- Não permitir **depósitos** ou **saques** com **valores negativos**;
- Limitar **saques** a um valor máximo de **R$ 500** por operação;
- Restringir o número de **saques** e **depósitos** em **10 por dia**;
- Registrar todas as movimentações em um **extrato** com data e hora da transação, acessível mediante solicitação do usuário.

---

### 🛠️ Versão 3: Evolução para Múltiplos Usuários e Contas

Nesta fase, o sistema passou por melhorias estruturais e novas funcionalidades:

#### ✅ Refatoração de Funções

- As funções de **saque**, **depósito** e **extrato** foram separadas em funções distintas.
- Foram criadas duas novas funções:
  - `criar_usuario()` — para cadastrar clientes;
  - `criar_conta_bancaria()` — para cadastrar contas bancárias.
  - `vincular_conta()` — para associar a conta ao usuário correspondente.


#### ⚙️ Regras Técnicas

- A função `saque` deve receber os argumentos **apenas por nome** (`keyword only`);
- A função `depósito` deve receber os argumentos **apenas por posição** (`positional only`);

---

#### 👤 Cadastro de Usuários

- Os **usuários** devem ser armazenados em uma **lista**;
- Cada usuário é composto por:
  - `nome`
  - `data de nascimento`
  - `cpf` (apenas números)
  - `endereço` (formato: `logradouro, nro - bairro - cidade/sigla estado`)
- Não é permitido cadastrar dois usuários com o **mesmo CPF**.

---

#### 🏦 Cadastro de Contas Bancárias

- As **contas bancárias** devem ser armazenadas em uma **lista**;
- Cada conta é composta por:
  - `agência` (valor fixo: `'0001'`)
  - `número da conta` (sequencial, iniciando em 1)
  - `usuário` (referência a um usuário existente)
- Um **usuário pode ter várias contas**, mas **uma conta pertence a apenas um usuário**.

---

#### 🔍 Vinculação de Contas

- Para vincular uma conta a um usuário, o sistema deve:
  - Solicitar o CPF
  - Procurar o CPF na lista de usuários
  - Se encontrado, associar a conta ao usuário correspondente

---

#### 📋 Listagem

- Para listar usuários e suas contas:
  - Filtrar a lista de usuários pelo número do CPF
  - Exibir as contas associadas a cada usuário

---

### ✅ Conclusão

Este projeto foi desenvolvido como parte do desafio prático da plataforma **DIO.ME**, reforçando conceitos de:
- Estruturação de código com funções
- Uso de listas e dicionários
- Entrada e saída de dados no terminal
- Boas práticas de programação em Python
