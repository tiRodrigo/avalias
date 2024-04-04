#NOTE - o que é uma classe?
    #Uma classe é uma forma de definir um tipo de dado em uma linguagem orientada a objeto. Ela é formada por dados e comportamentos.

#NOTE - Quais as vantagens de utulizar uma classe?
    #As principais vantagens é facilitar a leitura e a manutenção.

#NOTE - Em uma programação funcional a classe é importante?
    #

#NOTE - o que vem a ser paradigma de programção?

#NOTE - o python é multi paradigma? Explique 

class Carro:
    def __init__(self, nome, marca):
        self._nome = nome
        self._marca = marca

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def get_marca(self):
        return self._marca

    def set_marca(self, nova_marca):
        self._marca = nova_marca

meu_carro = Carro(nome="xxxx", marca="xxxxxx")
print(f"Nome do carro: {meu_carro.get_nome()}")
print(f"Marca do carro: {meu_carro.get_marca()}")




