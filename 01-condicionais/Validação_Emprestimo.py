#Validação de Empréstimo Bancário

nome = input('Digite o seu nome? ')

idade = int(input('Digite a sua idade? '))
if idade < 21:
   print('Sua idade não corresponde ao exigido')
   exit()
else:
    print('Idade corresponde ao exigido')
    
emprestimo = float(input('Digite o valor do emprestimo? '))
if emprestimo >= 1000 and emprestimo <= 50000:
    print("Valor correspondeao exigido")
else:
    print('Valor não corresponde ao exigido')
    exit()

tempo = int(input('Digite quantas parcelas? '))
if tempo <= 0:
    print('Quantidade de parcelas invalida')
else:
    print('Quantidade de parcelas registrada')

renda = float(input('Digite o valor da sua renda? '))
if renda <= 0:
    print('Valor de renda Invalida')
    exit()
else: 
    print('Valor da renda Aprovado')

parcela = emprestimo / tempo
total = renda * 0.30
if total >= parcela:
   print('Aprovado o emprestimo')
else: 
    print('Reprovado o emprestimo')
