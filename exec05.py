somatorio = 0

for i in range(1, 6):
    num = float(input(f"Digite o {i}º valor: "))
    if num < 10:
        somatorio += num

print(f"O somatório dos valores menores que 10 é: {somatorio}")