#Crie um programa que solicite dois números do usuário e exiba a soma, subtração, multiplicação e divisão desses números.
#Minha solução
# num_user = input('Digite um numero: ')
# num1_user = input('Digite outro numero: ')

# num = int(num_user)
# num1 = int(num1_user)

# print(num + num1)
# print(num - num1)
# print(num * num1)
# print(num / num1)

#Solução gpt
while True:
    
    try:
        num_user = input('Digite um numero: ')
        num1_user = input('Digite outro numero: ')


        num = int(num_user)
        num1 = int(num1_user)
        
        print(f'A soma dos dois numeros é: ', num + num1)
        print(f'A subtração dos dois numeros é: ', num - num1)
        print(f'A multiplicação dos dois numeros é: ', num * num1)
        # Divisão por zero gera erro.
        if num1 != 0:
            print(f'A divisão dos dois numeros é: {num / num1:.2f}') #Esse ajuste é meu.
        else:
            print(f'Não pode ser dividido por 0')

    except ValueError:
        print('Digite um número inteiro.')
    
    continu = input('Deseja continuar? s/n: ')
    if continu.lower() != 's':
        print('Saindo da aplicação.')
        break    