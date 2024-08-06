class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.pags = paginas

    def alterarEditora(self,nova_Editora):
        self.editora = nova_Editora
        return self.editora
    
    def listar_qtde_Paginas(self):
        return self.pags
    
livro1 = Livro("A Culpa é das Estrelas", "John Green","Intrínseca",288)
print(livro1.editora)

print(f"o nome do livro é {livro1.nome} seu autor é {livro1.autor} sua editora é {livro1.editora}, e sua qtde de pags é {livro1.pags}")

