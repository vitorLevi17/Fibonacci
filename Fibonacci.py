def ver_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return f'O número {numero} pertence à sequência de Fibonacci.'
    else:
        return f'O número {numero} não pertence à sequência de Fibonacci.'
acao = 1
while acao == 1:
    numero = int(input('Digite um número para verificar se ele pertence à sequência de Fibonacci: '))
    resultado = ver_fibonacci(numero)
    print(resultado)
    acao = int(input('Digite 0 para sair e 1 para continuar'))

