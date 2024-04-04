import flet as ft
def main(page:ft.Page):

    #Passo 1: definir 3 variáveis
    nome_maquina=""
    tempo_uso=""
    ligado=False

    #Passo 2 = Ler valores - Criar caixas de texto
    nome_text = ft.TextField (label="Digite o modelo")
    tempo_text = ft.TextField(label="Tempo de Uso(min)")
    ligado_text = ft.TextField(label="Ligado=True or False")
        
    page.window_width = 250
    page.window_height = 400
    page.bgcolor = "White"

    #passo 3 - mostrar os valores.
    #definir um click
    #Definir um botão com click
    #Mostrar a mensagem
    msg_1 = ft.Text(color="black")
    msg_2 =ft.Text(color="black")
    msg_3 = ft.Text(color="black")
    def btn_click(e):
            nome = nome_text.value
            tempo = int(tempo_text.value)
            ligado = bool(ligado_text.value)

            msg_1.value = f"nome:{nome_maquina} o tipo é:{type(nome)}"
            msg_2.value = f"tempo:{tempo_uso} o tipo é:{type(tempo)}"
            msg_3.value = f"ligado: {ligado} o tipo é: {type(ligado)}"
    
            page.update()

    

        #res = "f{nome_text}"

    btn = ft.ElevatedButton("Click aqui",on_click=btn_click)
    page.add(nome_text,tempo_text,ligado_text,btn,msg_1,msg_2,msg_3)
    page.update()
ft.app(target=main)
    # Atualizar página = page.update()