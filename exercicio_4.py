#Crie um programa que solicite ao usuário três notas e exiba a média dessas notas.
#Minha solução.
while True:
    
    print('Por favor, insira as notas das provas logo abaixo:')
    try:
        str_exam_grade1 = input('Por favor, insira a nota da primeira prova: ') #agora insira a nota da segunda ...
        str_exam_grade2 = input('Por favor, insira a nota da segunda prova: ')
        str_exam_grade3 = input('Por favor, insira a nota da terceira prova: ')

        num_exam_grade1 = float(str_exam_grade1)
        num_exam_grade2 = float(str_exam_grade2)
        num_exam_grade3 = float(str_exam_grade3)

        print('Pensando...')

        media = (num_exam_grade1 + num_exam_grade2 + num_exam_grade3) / 3

        print(f'A media do aluno foi: {media:.2f}')
    except ValueError:
        print('Digite somente números por favor.')
        
    continu = input('Deseja continuar? s/n: ')
    if continu.lower() != 's':
        print('Saindo da aplicação.')
        break
        