import flet as ft


lista_compras = ["arroz", "feijão", "quiabo"]
lista_compras.pop(2)  # Remove o item no índice 2 (quiabo)
indice_feijao = lista_compras.index("feijão")
print(f"O feijão está no índice {indice_feijao}")
quantidade_arroz = lista_compras.count("arroz")
print(f"O arroz aparece {quantidade_arroz} vezes na lista")
lista_compras.sort()
print("Lista ordenada:", lista_compras)
lista_compras.reverse()
print("Lista invertida:", lista_compras)