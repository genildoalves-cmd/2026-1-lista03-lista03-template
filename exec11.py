print("Este programa calcula o somatório de uma sequência de números.")
total = int(input("Digite o total de números a serem somados: "))

numeros = []
for i in range(total):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

soma = sum(numeros)

# Transforma a lista de números em texto unida por '+'
expressao = "+".join(map(str, numeros))
print(f"Saída no terminal: {expressao}={soma}")