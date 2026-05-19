somatorio = 0

for i in range(1, 6):
    num = int(input(f"Digite o {i}º número inteiro: "))
    if num % 2 == 0:
        somatorio += num

print(f"O somatório dos números pares é: {somatorio}")