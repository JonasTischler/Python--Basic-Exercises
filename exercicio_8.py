# #Crie um programa que solicite um número inteiro do usuário e exiba a tabuada desse número (de 1 a 10).
# #Minha solução.
# num_str = input('Insira um numero inteiro para exibir a tabuada de 1 a 10: ')
# try:
#     num = int(num_str)

#     print(f'A taboada do número {num_str} é:')
#     print(num * 1)
#     print(num * 2)
#     print(num * 3)
#     print(num * 4)
#     print(num * 5)
#     print(num * 6)
#     print(num * 7)
#     print(num * 8)
#     print(num * 9)
#     print(num * 10)

# except ValueError:
#     print('Por favor, digite um número inteiro.')    

    #Solução gpt.
while True:
    
    num_str = input('Insira um numero inteiro para exibir a tabuada de 1 a 10: ')
    try:
        num = int(num_str)
        print(f'A taboada do número {num_str} é:')
        for i in range(1,11): #for é bom para looping.
            print(f'A tabuada do número {num} vezes {i} é {num*i}.') #Os textos são meus.   
    except ValueError:
        print('Por favor, digite um número inteiro.')
        
    continu = input('Deseja continuar? s/n: ')
    if continu.lower() != 's':
        print('Saindo da aplicação.')
        break
        