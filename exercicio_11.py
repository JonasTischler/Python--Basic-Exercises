#Escreva um programa que verifique se uma palavra fornecida pelo usuário é um palíndromo (uma palavra que é igual quando lida de trás para frente, como "arara").
#Minha solução.
while True:
    
    user_word = input('Digite uma palavra para verificação de palíndromo: ')
    user_word_lower = user_word.lower()

    print(f'A palavra escolhida foi: {user_word}')
    palind_word = user_word_lower[::-1]
    if user_word_lower == palind_word:
        print('É uma palavra palíndroma ')
    else:
        print(f'Não é uma palavra palídroma. A palavra escolhida ao contrário é {palind_word}')
        
    continu = input('Deseja continuar? s/n: ')
    if continu.lower() != 's':
        print('Saindo da aplicação.')
        break  
    
   