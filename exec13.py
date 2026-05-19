num = int(input("Entrada: "))
saida = []

for i in range(1, 11):
    saida.append(f"{i}x{num}={i * num}")

print("Saída:", "; ".join(saida) + ";")