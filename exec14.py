linhas = int(input("Entrada: "))

print("Saída:")
# Parte crescente do triângulo
for i in range(1, linhas + 1):
    print("* " * i)

# Parte decrescente do triângulo
for i in range(linhas - 1, 0, -1):
    print("* " * i)