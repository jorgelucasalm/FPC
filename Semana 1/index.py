# Pegando os dois valores (X e Y) e adicionando em suas respectivas variaveis
#
# Caso o usuário coloque mais de dois valores irá aparecer um erro!
x, y = map(int, input().split())


def mult(x, y):
    if y == 1:
        return x
    else:
        return mult(x, y-1) + x


print(mult(x, y))
