# Projeto: Sistema de Validação de Empréstimo Bancário | Autor: Marcus Vinícius

nome = input('Digite o seu nome? ')

idade = int(input('Digite a sua idade? '))
if idade < 21: # É necessário que o cliente tenha no mínimo 21 anos ou mais.
   print('Sua idade não corresponde ao exigido')
   exit()
else:
    print('Idade corresponde ao exigido')
    
emprestimo = float(input('Digite o valor do emprestimo? '))
if emprestimo >= 1000 and emprestimo <= 50000: # O valor do emprestimo não pode menor que R$ 1.000,00 reais e não pode ser maior que R$ 50.000,00 reais
    print("Valor corresponde ao exigido")
else:
    print('Valor não corresponde ao exigido')
    exit()

tempo = int(input('Digite quantas parcelas? '))
if tempo <= 0: # A quantidade de parcelas não pode ser menor ou igual a 0
    print('Quantidade de parcelas invalida')
else:
    print('Quantidade de parcelas registrada')

renda = float(input('Digite o valor da sua renda? '))
if renda <= 0: # O valor da renda não pode ser menor ou igual a 0
    print('Valor de renda Invalida')
    exit() 
else: 
    print('Valor da renda Aprovado')

parcela = emprestimo / tempo # A parcela é básicamente o emprestimo dividido pelo tempo que o cliente solicitou 
total = renda * 0.30 # A renda é multiplicada por 30% para termos o valor total que o cliente consegue pagar baseado na sua renda
if total >= parcela: # O total que seria a renda multiplicada por 30% tem que ser maior ou igual o valor da parcela indicada pelo bando
   print('Aprovado o emprestimo')
else: 
    print('Reprovado o emprestimo')
