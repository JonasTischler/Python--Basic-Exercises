# #Crie um programa que faça uma contagem regressiva de 10 até 1, e ao final exiba a mensagem "Feliz Ano Novo!".
#Minha solução.
# enter_str = input('Digite qualquer ENTER para iniciar a contagem.')
# contador = 11

# while contador <= 11:
#     contador -= 1
#     if contador == 10:
#         print('10')
#     if contador == 9:
#         print('9')    
#     if contador == 8:
#         print('8')        
#     if contador == 7:
#         print('7')    
#     if contador == 6:
#         print('6')
#     if contador == 5:
#         print('5')
#     if contador == 4:
#         print('4')        
#     if contador == 3:
#         print('3')
#     if contador == 2:
#         print('2')
#     if contador == 1:
#         print('1')
#     if contador == 0:
#         print('0')               
#         break
# print('Feliz Novo Ano!')

    #Solução gpt.
while True:   
     
    enter_str = input('Pressione ENTER para iniciar a contagem regressiva.')
    contador = 10

    while contador > 0:
        print(contador)
        contador -= 1

    print('Feliz Ano Novo!')
    
    continu = input('Deseja continuar? s/n: ')
    if continu.lower() != 's':
        print('Saindo da aplicação.')
        break
    