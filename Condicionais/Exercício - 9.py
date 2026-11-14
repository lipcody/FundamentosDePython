# Entrada
print("")
print("")
print("================================================================")
print("Programa para calcular o reajuste salarial de um funcionário")
print("================================================================")
print("")

salario = float(input("   Digite o salário do funcionário: "))

#Processamento

if salario < 500 :
    salario = salario * 1.3
    print("")
    print("================================================================")
    print("PARABÉNS! Você recebeu um aumento de 30% no seu salário.")
    print("================================================================")
    print("")
    print(f"   Salário reajustado: {salario:.2f}")
    print("")
else:
    print("Funcionário não possui direito ao reajuste salarial")

