soma_pares = 0
soma_impares = 0

for i in range(1, 11):
    num = int(input(f"Digite o {i}º número inteiro: "))
    if num % 2 == 0:
        soma_pares += num
    else:
        soma_impares += num

print(f"Somatório dos números pares: {soma_pares}")
print(f"Somatório dos números ímpares: {soma_impares}")

if soma_impares > soma_pares:
    print("O somatório dos números ímpares é MAIOR do que o dos pares.")
elif soma_impares < soma_pares:
    print("O somatório dos números ímpares é MENOR do que o dos pares.")
else:
    print("O somatório dos números ímpares é IGUAL ao dos pares.")