limite = int(input("Digite um valor limite: "))

for i in range(1, limite + 1):
    if i % 3 == 0 and i % 7 == 0:
        print("POW")
    elif i % 3 == 0:
        print("PI")
    elif i % 7 == 0:
        print("PA")
    else:
        print(i)