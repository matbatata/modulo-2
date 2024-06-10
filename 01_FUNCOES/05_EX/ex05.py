def calcular_volume_esfera(raio):
    pi = 3.1414592
    volume = (4/3) * pi * (raio ** 3)
    return volume

raio = float(input("Insira o raio da esfera (em metros): "))
volume = calcular_volume_esfera(raio)
print("O volume da esfera é:", volume)

# falotu main(). De resto muito bom
