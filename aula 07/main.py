import random 

Q = []

for i in range(20):
    Q.append(random.randint(1,100))

if Q: 
    max_value, max_position = max(Q), Q.index(max(Q)) + 1
    min_value, min_position = min(Q), Q.index(min(Q)) + 1

    print(f'O maior elemento é {max_value} na posição {max_position}') 
    print(f'O menor elemento é {min_value} na posição {min_position}') 
else: 
    print('Não foram fornecidos números positivos')