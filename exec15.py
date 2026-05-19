pares = 0
impares = 0

while True:
    num = int(input("Digite um número (negativo para parar): "))
    if num < 0:
        break
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")