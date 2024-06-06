def calcular_volume_cilindro(altura, raio):
    pi = 3.1414592
    v = pi * raio ** 2 * altura
    return v

altura = 5
raio = 2
v = calcular_volume_cilindro(altura, raio)
print("O volume do cilindro é:", v)
