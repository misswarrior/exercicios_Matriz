matriz = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

for linha in range(5):
    for coluna in range(5):
        if coluna == linha:
            matriz[linha][coluna] = 1

for linha in matriz:
    print(linha)




