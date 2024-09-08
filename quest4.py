#o programa adquire 10 algarismos e os organiza dentro de 4 listas os mostra com base nas condições

pares = []
impares = []
positivos = []
negativos = []

for i in range(10):
    num = float(input("digite um numero: "))

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    if num > 0:
        positivos.append(num)
    else:
        negativos.append(num)

print(f"\nNumeros pares: {pares}")

print(f"\nNumeros ímpares: {impares}")

print(f"\nNumeros positivos: {positivos}")

print(f"\nNumeros negativos: {negativos}")
