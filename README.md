# 📚 Sistema de Aluguel de Livros

Este é um sistema simples de gerenciamento de biblioteca, permitindo o cadastro, edição, exclusão, aluguel e devolução de livros. Além disso, é possível gerenciar usuários que utilizam o sistema.

## 🚀 Funcionalidades

- 📖 **Gerenciamento de Livros:**
  - Cadastrar livros com título e autor.
  - Editar informações de um livro cadastrado.
  - Excluir livros do sistema.
  - Listar todos os livros cadastrados.
  - Alugar e devolver livros.
  
- 👤 **Gerenciamento de Usuários:**
  - Cadastrar usuários com nome e e-mail.
  - Editar informações de um usuário cadastrado.
  - Excluir usuários do sistema.
  - Listar todos os usuários cadastrados.

## 🛠️ Tecnologias Utilizadas

- **Python** 🐍
- **Orientação a Objetos (OOP)**
- **Manipulação de Listas e Estruturas de Dados**

## 📌 Exemplos de Uso

### **Cadastro de Livros e Usuários**
```python
sistema = SistemaAluguel()

sistema.cadastrar_livro("Os Segredos da Mente Milionária", "T. Harv Eker")
sistema.cadastrar_livro("O Homem Mais Rico da Babilônia", "George Samuel Clason")

sistema.cadastrar_usuario("Gabriel Dzuman", "gabriel@email.com")
sistema.cadastrar_usuario("Leonardo Dzuman", "leonardo@email.com")
```

### **Aluguel e Devolução de Livros**
```python
sistema.alugar_livro(1, 1)
sistema.devolver_livro(1)
sistema.alugar_livro(1, 1)
```

### **Listar Livros e Usuários**
```python
sistema.listar_livros()
sistema.listar_usuarios()
```

## 📜 Estrutura do Código

- **`Livro`**: Classe representando um livro com ID, título, autor e status de disponibilidade.
- **`Usuario`**: Classe representando um usuário com ID, nome e e-mail.
- **`SistemaAluguel`**: Classe principal que gerencia os livros e usuários.
  - Métodos para cadastro, edição, exclusão, listagem, aluguel e devolução de livros.
  - Métodos para cadastro, edição, exclusão e listagem de usuários.

## 📌 Melhorias Futuras
- 🔍 Implementar pesquisa avançada de livros e usuários.
- 🗃️ Utilizar um banco de dados para persistência dos dados.
- 🌐 Criar uma interface gráfica para facilitar a interação.


✍️ Desenvolvido por **Gabriel Dzuman** 🚀

