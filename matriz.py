matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = int(input("Digite um valor inteiro: "))

contador = 0

for linha in range(4):
    for coluna in range(4):
        if matriz[linha][coluna] > 10:
            contador += 1

for indice in range(4):
    print(matriz[indice])

print(contador)

