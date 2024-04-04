import flet as ft

def main(page:ft.Page):
    texto= ft.TextField(width=200,height=30)
    msg=ft.Text("Digite seu nome de qualquer forma!")
    def btn_click(e):
        msg.value = texto.value.upper()
        page.update()
    btn1 = ft.ElevatedButton("Tranformar minuscula",width=200,on_click=btn_click)
    page.update()
    page.add(msg,texto,btn1)
    
ft.app(target=main)



