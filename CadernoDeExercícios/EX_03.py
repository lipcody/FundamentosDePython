#Quatro operações: solicite dois números e apresente os resultados da soma, subtração, multiplicação e divisão. Considere o segundo número diferente de zero.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num2 != 0:
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2

    print(f"   Soma: {soma}")
    print(f"   Subtração: {subtracao}")
    print(f"   Multiplicação: {multiplicacao}")
    print(f"   Divisão: {divisao}")
else:
    print("Erro: O segundo número não pode ser zero.")