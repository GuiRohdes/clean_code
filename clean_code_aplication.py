def titulo():
    print('''...:::CALCULADORA INICIADA:::...''')
...

titulo()

def calculate():
    operation = input('''
Qual a operação deseja realizar:
+ para soma
- para subtração
* para multiplicação
/ para divisão
''')
    number_1 = int(input('Digite o primeiro número: '))
    number_2 = int(input('Digite o segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Opção inválida, tente novamente.')

    again()

def again():
    calculate_again = input('''
Deseja realizar um novo cálculo?  S para SIM ou N para NÃO.
''')

    if calculate_again.upper() == 'Y':
        calculate()
    elif calculate_again.upper() == 'N':
        print('Até logo.')
    else:
        again()

calculate()
