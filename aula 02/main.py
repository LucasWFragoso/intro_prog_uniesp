if __name__ == "__main__":
    # 1
    # number = float(input('digite um número: '))

    # if number > 10:
    #     print('seu número é maior que 10')
    # elif number == 10:
    #     print('seu número é igual a 10')
    # else:
    #     print('seu número é menor que 10')

    # 2
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2)/ 2

    if 10 >= media >= 6:
        print(f'Você foi aprovado,  com média: {media}')
    elif 0 <= media < 6:
        print(f'Você foi reprovado,  com média: {media}')
    else:
        print(f'Valor da media inválido, média: {media}')

    