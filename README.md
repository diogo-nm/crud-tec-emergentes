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
```
---

## 🖥 Ambiente de Desenvolvimento

- Sistema operacional: Windows 10 / Ubuntu 20.04 / macOS Catalina  
- Python 3.10  
- IDE: Visual Studio Code  

## 🚀 Como instalar e executar

1. Clone o repositório:  
   `git clone https://github.com/diogo-nm/crud-tec-emergentes.git`  
2. Acesse a pasta do projeto:  
   `cd crud-tec-emergentes`  
3. Crie um ambiente virtual (opcional, mas recomendado):  
   `python -m venv venv`  
   `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows)  
4. Instale as dependências:  
   `pip install -r requirements.txt`  
5. Execute a aplicação:  
   `python app.py` ou `flask run`  
6. Acesse `http://localhost:5000` no navegador

## 💻 Requisitos do Sistema

- Python 3.8 ou superior  
- 100 MB de espaço em disco disponível  
- Navegador moderno (Chrome, Firefox, Edge)

## 🤝 Como contribuir

- Faça um fork deste repositório  
- Crie uma branch com sua feature: `git checkout -b feature/nova-funcionalidade`  
- Faça commit das suas alterações: `git commit -m 'Adiciona nova funcionalidade'`  
- Envie para o seu fork: `git push origin feature/nova-funcionalidade`  
- Abra um Pull Request para o repositório original

## 🧹 Práticas de Código Limpo

- Código modularizado em funções e classes  
- Nomes de variáveis e funções claros e autoexplicativos  
- Comentários explicativos onde necessário  
- Separação clara entre lógica e apresentação (uso de templates Jinja2)  

## 🧪 Testes Automatizados

- Atualmente, testes automatizados não implementados  
- Planejamento para incluir testes unitários usando pytest no futuro

## 🏗 Padrão de Projeto Aplicado

- Uso do padrão MVC (Model-View-Controller) simplificado, com separação entre lógica de negócios (app.py), visualização (templates) e dados (SQLite)

