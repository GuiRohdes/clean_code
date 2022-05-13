def titulo():
    print('''
...:::CALCULADORA INICIADA:::...
''')
...

titulo()

def soma():
  print('{} + {} = '.format(n1, n2))
  print(n1 + n2)

def calculate():
    operation = input('''
Qual a operação deseja realizar:
+ para soma
- para subtração
* para multiplicação
/ para divisão
''')
    #Solicita que o usuário digite os números que deseja calcular.
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    #Realiza a soma
    if operation == '+':
      soma()
    #Realiza a subtração
    elif operation == '-':
        print('{} - {} = '.format(n1, n2))
        print(n1 - n2)
    #Realiza a multiplicação
    elif operation == '*':
        print('{} * {} = '.format(n1, n2))
        print(n1 * n2)
    #Realiza a divisão
    elif operation == '/':
        print('{} / {} = '.format(n1, n2))
        print(n1 / n2)
    #Caso o usuário utilize uma operação inválida o programa irá fechar.
    else:
        print('Opção inválida, tente novamente.')

    again()

#Função para reiniciar ou finalizar o programa.
def again():
    calc_again = input('''
Deseja realizar um novo cálculo?  S para SIM ou N para NÃO.
''')
      ##Upper para tranformar em maiúscula
    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até logo')
    else:
        again()

calculate()