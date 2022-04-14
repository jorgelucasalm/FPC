# classes Biblioteca e Livro:
# - A Biblioteca contem uma lista de livros disponiveis e uma lista de livros alugados
# - A biblioteca possui um metodo para alugar um livro. Caso o livro jah esteja alugado a pessoa nao poderah alugar este livro.
# - A biblioteca possui um metodo para devolver o livro.
# - A biblioteca possui um metodo que devolve o nome do livro mais alugado.

class Livro:
    codigo = None
    nome = None
    autor = None
    __qtdeAlugueis = 0

    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor

    def incrementaAluguel(self):
        self.__qtdeAlugueis += 1

    def getQtdeAlugueis(self):
        return self.__qtdeAlugueis


class Biblioteca:
    alugados = []
    disponiveis = []

    def inserir(self, livro):
        self.disponiveis.append(livro)

    def alugar(self, livro):
        ok = True
        mensagem = None
        if livro in self.disponiveis:
            for i in self.disponiveis:
                if i == livro:
                    i.incrementaAluguel()
                    self.alugados.append(i)
                    self.disponiveis.remove(i)
                    break
        elif livro in self.alugados:
            ok = False
            mensagem = "O livro ja esta alugado, infelizmente voce nao podera alugar"
        else:
            ok = False
            mensagem = "O livro nao existe"
        return (ok, mensagem)

    def devolver(self, codLivro):
        ok = True
        mensagem = None
        for livro in self.alugados:
            if livro.codigo == codLivro:
                self.disponiveis.append(livro)
                self.alugados.remove(livro)
                break
        else:
            ok = False
            mensagem = "O livro nao esta alugado"
        return (ok, mensagem)

    def livroMaisAlugado(self):
        ok = True
        mensagem = None
        maior = 0
        nome = None
        for livro in self.disponiveis:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        for livro in self.alugados:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        if maior == 0:
            ok = False
            mensagem = "Nenhum livro foi alugado ainda"
        else:
            mensagem = "O livro mais alugado e: %s (%d alugueis)" % (
                nome, maior)
        return (ok, mensagem)

    def livrosOrdenadosPeloNome(self):
        arr = []
        i = j = 0
        ld = self.disponiveis
        la = self.alugados

        for j in range(len(ld)-1):
            for i in range(len(ld)-1):
                if ld[i].nome.lower() > ld[i+1].nome.lower():
                    ld[i], ld[i+1] = ld[i+1], ld[i]

        for j in range(len(la)-1):
            for i in range(len(la)-1):
                if la[i].nome.lower() > la[i+1].nome.lower():
                    la[i], la[i+1] = la[i+1], la[i]

        if len(ld) > 0 and len(la) > 0:
            for j in range(len(la)):
                for i in range(len(ld)):
                    if la[i].nome.lower() > ld[j].nome.lower():
                        arr.append(ld[j])
                    else:
                        arr.append(la[i])
            return arr
        if len(ld) > 0 or len(la) > 0:
            if len(ld) > 1:
                return ld
            if len(la) > 1:
                return la


# exemplo de execucao:
b = Biblioteca()

inp = input().split(',')
x = inp[0]
inp.remove(inp[0])

for i in range(len(inp)):
    if i % 3 == 0:
        b.inserir(Livro(inp[i], inp[i+1], inp[i+2]))

arr = b.livrosOrdenadosPeloNome()
newArr = []
for i in range(len(arr)):
    newArr.append((arr[i].codigo))

print(' '.join(newArr))
