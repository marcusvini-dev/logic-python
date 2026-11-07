#Calculadora de multa da biblioteca

atraso = int(input("Quantos dias de atraso? "))
if atraso < 0:
    print("Dias inválidos")
    exit()  # dias inválidos: encerra o programa

usuario = input("Tipo de usuário (aluno / professor)? ")
if usuario != "aluno" and usuario != "professor":
    print("Tipo inválido")
    exit()  #ipo inválido: encerra o programa

# Decisão 1: valor por dia
if atraso <= 5:
    valor_dia = 2.00
else:
    valor_dia = 3.00

total_multa = atraso * valor_dia

# Decisão 2: desconto pelo tipo
if usuario == "professor":
    desconto = 0.50
else:
    desconto = 0.00

total_desconto = total_multa * desconto
total = total_multa - total_desconto
print(f"Total a ser pago: {total:.2f}")
