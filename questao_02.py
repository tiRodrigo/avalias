
import flet as ft

nome = input("Digite o nome: ")
if nome.isalpha() or nome.isspace():
    print("Nome em letras Maiúscula:", nome.upper())


