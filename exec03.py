inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

somatorio = 0

print("Números no intervalo:")
for i in range(inicio, fim + 1):
    print(i, end=" ")
    somatorio += i

print(f"\nO somatório dos números é: {somatorio}")