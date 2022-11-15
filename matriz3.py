matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

for linha in range(4):
    for coluna in range(4):
        produto = linha * coluna
        matriz[linha][coluna] = produto

for line in matriz:
    print(line)
