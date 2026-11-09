#conversor de moeda 

moeda = (input("Qual o tipo de moeda você quer fazer oo câmbio Dolar / Euro / Libra / Real? "))
quantidade = float(input("Qual a quantidade? "))

#quantidade < 0
if quantidade >=1:
    print("Valor  Válido")
else:
    print("valor Invalido")
    exit() #finaliza conversa 
#valor da moeda
if moeda == "Dolar":
   valor = 5.30
elif moeda == "Euro":
   valor = 6.40
elif moeda == "Libra":
   valor = 7.20
elif moeda == "Real":
   valor = 3.40
else:
    print("Moeda não cadastrada")
    exit() #finaliza conversa 

total = valor * quantidade
print(f" O total a receber é de {total}")
