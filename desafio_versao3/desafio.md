# 💳 Sistema Bancário Simples em Python (VILAVELHA)

Este é o desafio que foi proposto inical pela dio.me ele é um sistema bancário simples desenvolvido em Python com funcionalidades básicas como cadastro de clientes, criação de contas, depósitos, saques e emissão de extrato bancário. O sistema utiliza conceitos de orientação a objetos e boas práticas de programação.

---

## 🧠 Funcionalidades
### Obrigatórias 
- Cadastro de cliente (Pessoa Física)
- Criação automática de conta corrente
- Realização de depósitos e saques
- Controle de limite de saque diário e valor máximo por saque
- Histórico de transações (extrato)
### Criadas por mim 
- Login
- Menu
- Validação básica de CPF

---

## ⚙️ Estrutura do Projeto

- **Cliente e Pessoa Física**: Gerencia os dados pessoais e as contas associadas.
- **Conta e Conta Corrente**: Gerencia saldo, saques, depósitos e regras de negócio.
- **Transações (Depósito/Saque)**: Aplicadas como comandos separados com registro no histórico.
- **Histórico**: Guarda as transações realizadas.
- **Validador**: Realiza verificação de CPF.
- **Menu e Login**: Interação com o usuário via terminal.

---

## 🔧 Requisitos

- Python 3.7+
- Terminal/Shell para rodar o script

---

## ▶️ Como Executar

1. Clone ou copie o código.
2. Salve-o como `sistema_bancario.py`
3. Execute no terminal:

---

## 🧠 Aprendizados e Experiência Pessoal

Este projeto foi desenvolvido como prática dos meus estudos em Python, com foco nos seguintes conceitos:

- Orientação a Objetos (classes, herança, encapsulamento)
- Uso de classes abstratas com `abc.ABC`
- Organização de responsabilidades entre objetos
- Manipulação de listas e atributos privados
- Criação de menus simples com interação via terminal
- Validação de entrada (como CPF)
- Registro de histórico com data e hora usando `datetime`

Ainda estou desenvolvendo minhas habilidades por isso contei com apoio de ferramentas que me ajudaram a estruturar melhor as seções técnicas e a resolver problemas que ja estavam gastando muito do meu tempo, mas sem deixa de lado objetivo princiapal que era o aprendizado pratico. Este projeto representa um passo importante na minha jornada de aprendizado.