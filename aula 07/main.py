import random 

# Q = []

# for i in range(20):
#     Q.append(random.randint(1,100))

# if Q: 
#     max_value, max_position = max(Q), Q.index(max(Q)) + 1
#     min_value, min_position = min(Q), Q.index(min(Q)) + 1

#     print(f'O maior elemento é {max_value} na posição {max_position}') 
#     print(f'O menor elemento é {min_value} na posição {min_position}') 
# else: 
#     print('Não foram fornecidos números positivos')

lista = []
resultado_da_soma = 0

for n in range(10):
    lista.append(random.randint(1,10))

for i in lista:
    if(i % 2) == 0:
        resultado_da_soma = resultado_da_soma + i

print(f'O resultado da soma é: {resultado_da_soma}')
print(lista)      