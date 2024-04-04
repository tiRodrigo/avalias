import flet as ft

def main(page: ft.Page):
    texto = ft.TextField(width=200, height=40)
    msg = ft.Text("Escolha um dia da semana de 1 a 7: ")

    def btn_click(e):
        numero = int(texto.value)
        if numero == 1:
            msg.value = "Domingo"
        elif numero == 2:
            msg.value = "Segunda-feira"
        elif numero == 3:
            msg.value = "Terça-feira"
        elif numero == 4:
            msg.value = "Quarta-feira"
        elif numero == 5:
            msg.value = "Quinta-feira"
        elif numero == 6:
            msg.value = "Sexta-feira"
        elif numero == 7:
            msg.value = "Sábado"
        else:
            msg.value = "Número inválido. Digite um valor entre 1 e 7."

        page.update()

    btn1 = ft.ElevatedButton("Dias da semana", width=200, on_click=btn_click)
    page.add(texto)
    page.add(msg)
    page.add(btn1)
    page.update()

ft.app(target=main)