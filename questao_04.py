import flet as ft

numero_semana = int(input("Digite um número de 1 a 7: "))

if numero_semana == 1:
    print("Dia: Domingo")
elif numero_semana == 2:
    print("Dia: Segunda-Feira")
elif numero_semana == 3:
    print("Dia: Terça-Feira")
elif numero_semana == 4:
    print("Quarta-feira")
elif numero_semana == 5:
    print("Quinta-Feira")
elif numero_semana == 6:
    print("Sexta-Feira")
elif numero_semana == 7:
    print("Sabado")
else:
    print("Valor Inválido")

