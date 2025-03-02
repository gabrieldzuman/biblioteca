import datetime

class Livro:
    def __init__(self, id, titulo, autor, disponivel=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def __str__(self):
        return f"ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Disponível: {'Sim' if self.disponivel else 'Não'}"


class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Email: {self.email}"


class SistemaAluguel:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.id_livro = 1
        self.id_usuario = 1

    def cadastrar_livro(self, titulo, autor):
        livro = Livro(self.id_livro, titulo, autor)
        self.livros.append(livro)
        self.id_livro += 1
        print(f"Livro '{titulo}' cadastrado com sucesso!")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
        for livro in self.livros:
            print(livro)

    def editar_livro(self, id, titulo=None, autor=None):
        livro = self.buscar_livro(id)
        if livro:
            if titulo:
                livro.titulo = titulo
            if autor:
                livro.autor = autor
            print("Livro editado com sucesso!")
        else:
            print("Livro não encontrado.")

    def excluir_livro(self, id):
        livro = self.buscar_livro(id)
        if livro:
            self.livros.remove(livro)
            print("Livro excluído com sucesso!")
        else:
            print("Livro não encontrado.")

    def cadastrar_usuario(self, nome, email):
        usuario = Usuario(self.id_usuario, nome, email)
        self.usuarios.append(usuario)
        self.id_usuario += 1
        print(f"Usuário '{nome}' cadastrado com sucesso!")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        for usuario in self.usuarios:
            print(usuario)

    def editar_usuario(self, id, nome=None, email=None):
        usuario = self.buscar_usuario(id)
        if usuario:
            if nome:
                usuario.nome = nome
            if email:
                usuario.email = email
            print("Usuário editado com sucesso!")
        else:
            print("Usuário não encontrado.")

    def excluir_usuario(self, id):
        usuario = self.buscar_usuario(id)
        if usuario:
            self.usuarios.remove(usuario)
            print("Usuário excluído com sucesso!")
        else:
            print("Usuário não encontrado.")

    def alugar_livro(self, id_livro, id_usuario):
        livro = self.buscar_livro(id_livro)
        usuario = self.buscar_usuario(id_usuario)

        if not livro or not usuario:
            print("Livro ou usuário não encontrado.")
            return

        if not livro.disponivel:
            print("O livro não está disponível para aluguel no momento.")
            return

        livro.disponivel = False
        print(f"Livro '{livro.titulo}' alugado por {usuario.nome} em {datetime.date.today()}.")

    def devolver_livro(self, id_livro):
        livro = self.buscar_livro(id_livro)

        if not livro:
            print("Livro não encontrado.")
            return

        if livro.disponivel:
            print("Este livro já está disponível na biblioteca.")
            return

        livro.disponivel = True
        print(f"Livro '{livro.titulo}' devolvido em {datetime.date.today()}.")

    def buscar_livro(self, id):
        for livro in self.livros:
            if livro.id == id:
                return livro
        return None

    def buscar_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario
        return None


# Exemplo de uso
sistema = SistemaAluguel()

sistema.cadastrar_livro("Os Segredos da Mente Milionária", "T. Harv Eker")
sistema.cadastrar_livro("O Homem Mais Rico da Babilônia", "George Samuel Clason")
sistema.cadastrar_usuario("Gabriel Dzuman", "gabriel@email.com")
sistema.cadastrar_usuario("Leonardo Dzuman", "leonardo@email.com")

sistema.alugar_livro(1, 2)
sistema.devolver_livro(1)
sistema.alugar_livro(1, 1)

sistema.listar_livros()
sistema.listar_usuarios()
