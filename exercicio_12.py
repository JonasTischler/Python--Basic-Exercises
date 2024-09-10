#Crie um programa que solicite um número inteiro e calcule o fatorial desse número.
# import math
# num_str = input('Digite um número inteiro para exibir o seu fatorial: ')
# num = int(num_str)

# print(math.factorial(num))
while True:    
    
    num_str = input('Digite um número inteiro para exibir o seu fatorial: ')
    num = int(num_str)
    def fatorial(n):
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    resultado_fatorial = fatorial(num)
    print(f'O fatorial de {num} é {resultado_fatorial}.')
    
    continu = input('Deseja continuar? s/n: ')
    if continu.lower() != 's':
        print('Saindo da aplicação.')
        break
