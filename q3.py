# Pergunte o valor de "n" para o usuário e salve-o como uma variável inteira.
n = int(input("n: "))

# Calcule a sequência de Collatz para esse número
seq = [n]
passos = 1
numeros = []
while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3*n + 1
    passos = passos +1
    numeros.append(n)

print("seq =", seq)

# Calcule quantos termos possui a sequência obtida
n_termos = passos
print("n termos =", passos)

# Diga qual é o maior valor atingido nesta sequência.
maior = max(numeros)
print("maior valor =", maior)
