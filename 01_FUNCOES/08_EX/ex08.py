def eh_quadrado_perfeito(numero):
    return int(numero ** 0.5) ** 2 == numero
def main():
    exemplos = [1, 4, 9, 10, 16, 25]
    for num in exemplos:
        if eh_quadrado_perfeito(num):
            print(num, "é um quadrado perfeito.")
        else:
            print(num, "não é um quadrado perfeito.")
main() 
