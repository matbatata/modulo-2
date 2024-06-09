def calcular_media(nota1, nota2, nota3, letra):
    if letra == "A":
        return (nota1 + nota2 + nota3) / 3
    elif letra == "P":
        return (nota1 * 5 + nota2 * 3 + nota3 * 2) / (5 + 3 + 2)
    else:
        return "Tipo de média inválido."
def main():
    notas = (7, 8, 9)
    tipo_media = "A"
    media = calcular_media(*notas, tipo_media)
    print("A média do aluno é:", media)
main()
