def imprimir_mes(numero):
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    
    if numero < 1 or numero > 12:
        print("Número inválido. Por favor, insira um número entre 1 e 12.")
    else:
        print(meses[numero])

n = int(input("Digite um número de 1 a 12: "))
imprimir_mes(n)

"""
PONTOS A MELHORAR:

1. Chamar a funbção main(). 
    Dica: Usar o 04_EX.py como exemplo
    
2. Eu não ensinei esse negócio de 1: "Janeiro", ..., 12: "Fevereiro"
    Duas opções:

    1) Quero que você escreva um .md explicando o que é e como funciona com as fontes que você usou para fazer isso...

    2) Fazer do jeito que aprendemos em sala.
"""
