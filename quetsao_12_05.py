import flet as ft

import flet as ft

def mes_correspondente(numero):
    match numero:
        case 1:
            return "Janeiro"
        case 2:
            return "Fevereiro"
        case 3:
            return "Março"
        case 4:
            return "Abril"
        case 5:
            return "Maio"
        case 6:
            return "Junho"
        case 7:
            return "Julho"
        case 8:
            return "Agosto"
        case 9:
            return "Setembro"
        case 10:
            return "Outubro"
        case 11:
            return "Novembro"
        case 12:
            return "Dezembro"
        case _:
            return "Número inválido. Digite um valor entre 1 e 12."

def btn_click():
    numero = int(texto.get_text())
    mes = mes_correspondente(numero)
    msg.set_text(f"O mês correspondente ao dia {numero} é: {mes}")

def main(page: ft.Page):
    global texto, msg
    texto = ft.TextField(width=200, height=40)
    msg = ft.Text("Escolha um dia do mês de 1 a 12: ")
    btn1 = ft.ElevatedButton("Mes do ano", width=200, on_click=btn_click)
    page.add(texto, msg, btn1, )
    page.update()
    

ft.app(target=main)
