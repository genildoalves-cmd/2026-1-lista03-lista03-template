resultados = []

for i in range(1000, 3001):
    if i % 7 == 0 and i % 5 != 0:
        resultados.append(str(i))

print(";".join(resultados))