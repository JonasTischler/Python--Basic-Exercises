#Escreva um programa que converta uma temperatura fornecida pelo usuário de graus Celsius para Fahrenheit. A fórmula de conversão é: procurar no google
#Minha solução
while True:
    
    try:
        temp_str = input('Digite a temperatura em graus Celsius para que seja convertido por Fahrenheit: ')
        temp_celsius = float(temp_str)
        fahr = temp_celsius * (9/5) + 32
        print(f' A temperatura de {temp_celsius:.2f} graus Celsius convertida para Fahrenheit é: {fahr:.2f}F°')
    except ValueError:
        print('Digite uma temperatura válida.')
        
    continu = input('Deseja continuar? s/n: ')
    if continu.lower() != 's':
        print('Saindo da aplicação.')
        break
        