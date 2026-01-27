print('=' * 35)
print('   Calculadora Simples em Python')
print('=' * 35)

def calcular(n1, n2, operador):
    if operador == '+':
        return n1 + n2
    elif operador == '-':
        return n1 - n2
    elif operador == '*':
        return n1 * n2
    elif operador == '**':
        return n1 ** n2
    elif operador == '/':
        if n2 == 0:
            return 'Erro: divisão por zero'
        return n1 / n2
    elif operador == '//':
        if n2 == 0:
            return 'Erro: divisão por zero'
        return n1 // n2
    else:
        return 'Operador inválido'

while True:
    try:
        n1 = float(input('\nDigite um número (0 para sair): '))
        n2 = float(input('Digite outro número (0 para sair): '))

        if n1 == 0 and n2 == 0:
            print('\nPrograma encerrado')
            break

        print('Operadores disponíveis: +  -  *  /  //  **')
        operador = input('Escolha um operador: ')

        resultado = calcular(n1, n2, operador)
        print('Resultado:', resultado)

    except ValueError:
        print('Erro: digite apenas números.')