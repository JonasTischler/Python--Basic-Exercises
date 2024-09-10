#Escreva um programa que solicite ao usuário seu peso (em kg) e altura (em metros), e calcule o Índice de Massa Corporal (IMC). A fórmula é:
#Minha solução
while True:
    
    try:
        print('Insira seu dados abaixo para calcular o seu IMC: ')
        name = input('Insira seu nome completo: ')
        weight_str = input('Insira seu peso em Kg: ')
        height_str = input('Insira sua altura em metros: ')
        weight = float(weight_str)
        height = float(height_str)
        imc = weight / (height * height)
        print(f'{name} seu IMC é {imc:.2f} ')
    except ValueError:
        print('Por favor, inserir valores validos para peso e altura.')
        
    continu = input('Deseja continuar? s/n: ')
    if continu.lower() != 's':
        print('Saindo da aplicação.')
        break
    