#Crie um programa que solicite ao usuário uma frase e conte quantas palavras há na frase.
#Não consegui ter solução. Não lembrava da função split e len para aplicar; 
    
# sentence = input('Digite uma frase pra contarmos quanta palavras tem: ')
# space_str = ' '
# space_int = int(space_str)
# i = 1 + 0

# num_of_word = i + space_int
# if space_int in sentence:
#     print(f'A frase tem {num_of_word} palavras.')

# # a cada espaço na frase digitada, temos 1+X espaços e assim da para determinar a contagem de palavras.
# # O 1 seria a palavra inicial que vem sem espaço. A menos que a pessoa digite de forma incomum,
# # mas igual daria para caso o teclado receber o sinal do espaço, contabilizar. 

while True:
    
    sentence = input('Digite uma frase pra contarmos quanta palavras tem: ')
    word = sentence.split() # Função split para contagem de palavras.
    word_num = len(word)
    print(f'A frase digitada contém {word_num} palavras.')
    
    continu = input('Deseja continuar? s/n: ')
    if continu.lower() != 's':
        print('Saindo da aplicação.')
        break

#Uma outra versão mais informada ao gpt, pela minha logica que nao havia função aplicada.
# # Solicita uma frase ao usuário
# frase = input('Digite uma frase: ')

# # Conta os espaços na frase
# numero_espacos = frase.count(' ')

# # O número de palavras seria o número de espaços + 1
# numero_palavras = numero_espacos + 1

# print(f'A frase contém {numero_palavras} palavras.')