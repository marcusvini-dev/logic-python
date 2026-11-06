#Desconto por quantidade

preco = float(input("Qual o preço do produto? "))
if preco <= 0:
    print("Valor Invalido")
    exit() #se o preço for menor que zero, invalida e encerra o código
quantidade = int(input("Qual a quantidade que você pretende levar? "))

if quantidade <=0:
    print("Quantidade Invalida")
    exit() #se a quantidade for menor que zero, invalida e encerra o código
elif quantidade >= 1 and quantidade <= 9:
    desconto = 0.00 #desconto 
elif quantidade >= 10 and quantidade <=49:
    desconto = 0.05 #desconto 
elif quantidade >= 50 and quantidade <=99:
    desconto = 0.10 #desconto 
elif quantidade >= 100:
    desconto= 0.15 #desconto 

total = preco * quantidade #soma de preço unitário do produto e multiplica pela quantidade de produtos que foi solicitado
final = total - (total * desconto) #vai pegar o total multiplicar pelo desconto e subtrair pelo valor total, dando o valor com o desconto de acordo com a quantidade solicitada pelo cliente 
print(f"O valor da compra com o desconto é de {final:.2f}")
