nome = input("Informe seu nome: ")
altura = float(input("Informe sua altura em M: "))
peso = float(input("Informe seu peso:"))

imc = peso / (altura * altura)

print(f"{nome}, o seu Índice de massa corporal é: {imc}")

