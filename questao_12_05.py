import flet as ft

def main(page: ft.Page):
    texto = ft.TextField(width=200, height=40)
    msg = ft.Text("Escolha um mês de 1 a 12: ")

    def btn_click(e):
        try:
            numero = int(texto.value)
            match numero:
                case 1:
                    msg.value = "Janeiro"
                case 2:
                    msg.value = "Fevereiro"
                case 3:
                    msg.value = "Março"
                case 4:
                    msg.value = "Abril"
                case 5:
                    msg.value = "Maio"
                case 6:
                    msg.value = "Junho"
                case 7:
                    msg.value = "Julho"
                case 8:
                    msg.value = "Agosto"
                case 9:
                    msg.value = "Setembro"
                case 10:
                    msg.value = "Outubro"
                case 11:
                    msg.value = "Novembro"
                case 12:
                    msg.value = "Dezembro"
                case _:
                    msg.value = "Número inválido. Digite um valor entre 1 e 12."
        except ValueError:
            msg.value = "Por favor, insira um número inteiro."
        page.update()

    btn1 = ft.ElevatedButton("Escolher mês", width=200, on_click=btn_click)
    page.add(texto, msg, btn1)

ft.app(target=main)

