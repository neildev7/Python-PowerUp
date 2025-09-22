# 🛠️ Automação de Cadastro de Produtos

Este projeto implementa um **processo de automação em Python** para login e inserção de produtos em um sistema web a partir de um arquivo CSV.  
A solução utiliza bibliotecas de automação e manipulação de dados, garantindo maior eficiência e padronização no fluxo de trabalho.  

Este projeto foi desenvolvido durante o curso **Jornada Python** da [Hashtag Treinamentos](https://www.hashtagtreinamentos.com/), como forma de aplicar conceitos de **automação, manipulação de dados e integração de processos**.

---

## 📌 Sobre o Projeto

O sistema realiza automaticamente:

- 🔑 **Login no site** com credenciais configuradas no script  
- 📂 **Leitura de dados** a partir de um arquivo `produtos.csv`  
- 📝 **Cadastro de produtos** com os seguintes atributos:  
  - Código  
  - Marca  
  - Tipo  
  - Categoria  
  - Preço unitário  
  - Custo  
  - Observações (opcional)  
- 🔄 **Execução repetitiva** para múltiplos registros  
- ⏳ **Controle de fluxo** com pausas e ajustes de coordenadas de tela  

---

## 🚀 Tecnologias Utilizadas

- **Python**  
- **PyAutoGUI** – automação da interface gráfica  
- **Pandas** – manipulação de dados tabulares  
- **CSV** – entrada estruturada de dados  

---

## 📂 Estrutura do Projeto
- codigo.py # Script principal da automação
- auxiliar.py # Utilitário para capturar coordenadas da tela
- produtos.csv # Base de dados de produtos

---

## ▶️ Como Usar

1. Clone o repositório e instale as dependências: pip install pyautogui pandas
2. Ajuste as coordenadas de clique de acordo com sua tela utilizando:
   python auxiliar.py
3. Execute a automação:
   python codigo.py

## Contato

- Linkedin: [Neil Lopes](https://www.linkedin.com/in/neil-lopes-4a33a5383)
- E-mail: **neillopes237@gmail.com**
- Instagram: **neilzsz**
---

> Este projeto foi desenvolvido como **parte do meu aprendizado em Python**, aplicando **lógica de programação**, conceitos de **automação de tarefas** e integração com **manipulação de dados via CSV**, além de contribuir para a construção do meu **portfólio profissional**.
