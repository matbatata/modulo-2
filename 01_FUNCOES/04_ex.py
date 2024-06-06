# perfeito
def calcular_volume_cilindro(altura, raio):
    pi = 3.1414592
    v = pi * (raio ** 2) * altura # só colocar op parêntestes para ser mais fácil de ler
    return round(v, 2) # coloquei um round para ficar bonito, use isso como padrão...


# aqui faltou a main()
def main():    
    altura = float(input("Insira a altura (em m): "))
    raio = float(input("Insira o raio (em m): "))
    v = calcular_volume_cilindro(altura, raio)
    print("O volume do cilindro é:", v)


# sempre chamar a main() no final
main()

# está no caminho certo, parabéns
