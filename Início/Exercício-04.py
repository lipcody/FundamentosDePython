# ENTRADA

nome = input("Informe seu nome: ")
altura = float(input("Informe sua altura em M: "))
peso = float(input("Informe seu peso:"))

# PROCESSAMENTO

imc = peso / (altura * altura)

#SAÍDA

print(f"{nome}, o seu Índice de massa corporal é: {imc}")

