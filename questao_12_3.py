

def main(page:ft.Page):
    mensagem= ft.Text("Saber o tipo : "width=200,height=30)
    nome_maquina = ft.TextField(label= "Digite o nome da máquina")
    tempo_uso = ft.TextField(label= "Digite o tempo de uso")
    ligado = ft.TextField(label= True)





    ft.app(target=main)


'''
nome_maquina = str("string")
tempo_uso = int(1)
ligado = bool(True)

print(type(nome_maquina))
print(type(tempo_uso))
print(type(ligado))
'''

'''
def quest03(page:ft.Page):
    mensagem01 = ft.Text("Nome da máquina:")
    nome_maquina = ft.TextField(label="Nome:")

    mensagem02 = ft.Text("Tempo de uso:")
    tempo_uso = ft.TextField(label="Tempo:")

    mensagem03 = ft.Text("Ligado")

    ligado = True

   


    def btn_click(e):

        mensagem001 = ft.Text(f"Nome: {nome_maquina} - Tipo: {type(nome_maquina)}")
        mensagem002 = ft.Text(f"Tempo de uso: {tempo_uso} - Tipo: {type(tempo_uso)}")
        mensagem003 = ft.Text(f"Estado: {ligado} - Tipo: {type(ligado)}")
        page.add(mensagem001, mensagem002, mensagem003)

    btn = ft.ElevatedButton("Verificar", on_click=btn_click)

    page.add(mensagem01,nome_maquina,mensagem02,tempo_uso,mensagem03,ligado, btn)


    

ft.app(quest03)
'''