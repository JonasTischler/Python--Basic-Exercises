#Escreva um programa que peça três números ao usuário e determine qual deles é o maior.
# #Minha solução.
# print('Digite três números para determinar qual é o maior.')
# num1_str = input('Primeiro número: ')
# num2_str = input('Segundo número: ')
# num3_str = input('Terceiro número: ')
# try:
#     num1 = float(num1_str)
#     num2 = float(num2_str)
#     num3 = float(num3_str)


#     if num1 > num2 and num1 > num3:
#         print(f'A primeira opção de número {num1} é o maior número.')
#     elif num2 > num1 and num2 > num3:    
#         print(f'A segunda opção de número {num2} é o maior número.')
#     elif num3 > num1 and num3 > num2:    
#         print(f'A terceira opção de número {num3} é o maior número.')
# except ValueError:
#     print('Por favor, digite um número válido.')
        
#Solução gpt. Houve uma outra solução na estrutura do if
while True:
    
    print('Digite três números para determinar qual é o maior.')
    num1_str = input('Primeiro número: ')
    num2_str = input('Segundo número: ')
    num3_str = input('Terceiro número: ')
    
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
        num3 = float(num3_str)

        if num1 == num2 == num3:
            print('Os três números são iguais. Digite novamente.') 
        elif num1 > num2 and num1 > num3:    
            print(f'A primeira opção de número {num1} é o maior número.')
        elif num2 > num1 and num2 > num3:    
            print(f'A segunda opção de número {num2} é o maior número.')
        else:
            print(f'A terceira opção de número {num3} é o maior número.')
    except ValueError:
        print('Por favor, digite um número válido.')
        
    continu = input('Deseja continuar? s/n: ')
    if continu.lower() != 's':
        print('Saindo da aplicação.')
        break
        