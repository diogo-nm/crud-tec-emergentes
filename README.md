# ✅ Projeto: SmartTasks

O **SmartTasks** é uma aplicação web simples para gerenciamento de tarefas, desenvolvida como parte da disciplina **Tecnologias Emergentes**. O sistema permite que o usuário **crie**, **visualize**, **atualize** e **exclua** tarefas — implementando as funcionalidades básicas de um sistema **CRUD** com persistência de dados em banco de dados relacional.

---

## 🎯 Objetivo da Aplicação

O objetivo do SmartTasks é fornecer uma plataforma prática e objetiva para o gerenciamento de tarefas do dia a dia. A aplicação permite ao usuário:

- Cadastrar novas tarefas com título, descrição e data de entrega
- Consultar a lista de tarefas cadastradas
- Editar dados de uma tarefa existente
- Remover tarefas concluídas ou não desejadas

O projeto busca aplicar na prática conceitos fundamentais de desenvolvimento web com back-end e front-end integrados.

---

## 🛠 Tecnologias Utilizadas

A aplicação foi desenvolvida com a seguinte stack de tecnologias:

| Tecnologia | Descrição |
|------------|-----------|
| **Python** | Linguagem principal de programação utilizada no back-end |
| **Flask** | Microframework web em Python para criação de rotas e lógica da aplicação |
| **SQLite** | Banco de dados leve utilizado para persistência local dos dados |
| **HTML5 + CSS3** | Utilizados para estruturar e estilizar a interface da aplicação |
| **Bootstrap** | Framework CSS para tornar a interface mais responsiva e moderna |
| **Jinja2** | Engine de templates utilizada pelo Flask para renderizar as páginas HTML |

---

## 📂 Estrutura do Projeto

```plaintext
smarttasks/
├── app.py           # Código principal da aplicação Flask
├── database.db      # Banco de dados SQLite
├── templates/       # Páginas HTML (com suporte a Jinja2)
├── static/          # Arquivos estáticos (CSS, imagens, etc.)
└── README.md        # Arquivo de documentação do projeto
