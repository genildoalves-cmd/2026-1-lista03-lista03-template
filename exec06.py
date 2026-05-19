somatorio = 0

for i in range(1, 6):
    num = float(input(f"Digite o {i}º valor: "))
    if num >= 10 and num < 20:
        somatorio += num

print(f"O somatório dos valores entre 10 e 19 é: {somatorio}")