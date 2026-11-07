nome = input("Informe seu nome: ")
print()
idade = int(input("Informe sua idade:"))
print()
salario = float(input("Informe seu salário: "))
print()

aumento = salario + (salario * 0.1)

print(f"PARABÉNS, {nome}. Aos {idade} anos de idade você acaba de receber um aumento de 10%.")
print(f"O seu novo salário vai ser de: R${aumento}")
print()
