qtd = int(input("Quantos valores você deseja digitar? "))
pares = 0

for i in range(1, qtd + 1):
    num = int(input(f"Digite o {i}º número inteiro: "))
    if num % 2 == 0:
        pares += 1

print(f"Você digitou {pares} número(s) par(es).")