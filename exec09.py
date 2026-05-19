soma_posicoes_impares = 0
soma_posicoes_pares = 0

for i in range(1, 11):
    num = float(input(f"Digite o {i}º valor: "))
    if i % 2 != 0:
        soma_posicoes_impares += num
    else:
        soma_posicoes_pares += num

print(f"Soma das posições ímpares (1ª, 3ª...): {soma_posicoes_impares}")
print(f"Soma das posições pares (2ª, 4ª...): {soma_posicoes_pares}")

if soma_posicoes_impares > soma_posicoes_pares:
    print("O somatório das posições ímpares é MAIOR que o das pares.")
elif soma_posicoes_impares < soma_posicoes_pares:
    print("O somatório das posições ímpares é MENOR que o das pares.")
else:
    print("Os somatórios são IGUAIS.")