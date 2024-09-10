# Escreva um programa que peça ao usuário para inserir um número e, em seguida, verifique se o número é par ou ímpar.
#Minha Solução
# num_user = input('Insira um número para verificar se é par ou impar: ')
# num = int(num_user)
# #O modulo retorna sempre o 
# resto = num % 2 
# if resto == 0:
#     print('O número é par.') 
# else:
#     print('O número é impar.')
 
#Solução gpt
while True:
    
    num_user = input('Insira um número para verificar se é par ou impar: ')

    try:    
        num = int(num_user)

        resto = num % 2 
        if resto == 0:
            print(f'O {num} é par.') 
        else:
            print(f'O {num} é impar.')
    except ValueError:
        print('Digite um numero válido inteiro.')
        
    continu = input('Deseja continuar? s/n: ')
    if continu.lower() != 's':
        print('Saindo da aplicação.')
        break    
    