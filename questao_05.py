
numero_mes = int(input("Digite um número de 1 a 12: "))

def mes_do_ano(numero):
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
            return "Valor inválido"

print(f"O mês correspondente ao número {numero_mes} é {mes_do_ano(numero_mes)}.")





