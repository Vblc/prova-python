"""
Explique no comentário porque o código do exemplo estava incorreto:

R: o progama falha pois podem ocorrer vários if ao mesmo tempo, causando respostas dupla.



"""

# Substitua os valores de A, B e C e modifique o código para corrigir
# os erros

A = 211
B = 62
C = 606
minABC = min(A, B, C)
maxABC = max(A, B, C)
n = 0
x = int(input("x: "))

if x == 0:
    print("nulo")
    n = n + 1
if x < 0:
    print("negativo")
    n = n + 1
elif x == 42:
    print("resposta para *a* pergunta")
    n = n + 1 
elif x > maxABC:
    print("grande")
    n = n + 1
if minABC < x < maxABC:
    print("médio")
    n = n + 1
if n == 0:
    print("nada de especial")
