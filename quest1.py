#duas maneira de usar estruturas de repetilção para construir uma tabuada

a = 1
n = input('digite um numero: ')

while a <= 10:
    resultado = a * int(n)
    print(f"{a} * {n} = {resultado}")
    a += 1    



n = input('digite um numero: ')

for i in range(10 + 1):
    resultado = i * int(n)
    print(f'{i} * {n} = {resultado}')
    i +=1