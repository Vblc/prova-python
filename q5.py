# Modifique o programa para remover o laço while e trocá-lo por um for.
x = float(input("x: "))
n = 0
resultado = 0.0
termo = 1.0

for n in range(0,5):
    n = n + 1
    termo = termo * x
    resultado = resultado + termo / n

print(resultado)
