matriz = [
    [1, 4, 0, 0],
    [7, 0, 10, 0],
    [0, 35, 0, 5],
    [2, 5, 20, 0]
]

maior = matriz[0][0]

linhaMaior = 0
colunaMaior = 0

for linha in range(4):
    for coluna in range(4):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
            linhaMaior = linha
            colunaMaior = coluna


for linha in matriz:
    print(linha)

print("O maior valor é: " + str(maior))
print("Ele está na linha : " + str(linhaMaior))
print("Ele está na coluna: " + str(colunaMaior))