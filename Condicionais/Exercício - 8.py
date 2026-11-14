# Faça um programa que receba o nome, cargo e salário de um funcionário. Se o funcionario ganhar abaixo de 1000 reais, calcule o salário acrescido de 10%. Ao final, exiba o nome, o cargo e o salário desse funcionário

nome = input("Digite o nome do funcionário: ")
cargo = input("Digite o cargo do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))

if salario < 1000:
    salario = salario * 1.1

    print("Seu salário recebido foi acrescido de 10%")
    print(f"Nome: {nome}")
    print(f"Cargo: {cargo}")
    print(f"Salário: {salario:.2f}")

else:
    print(f"Nome: {nome}")
    print(f"Cargo: {cargo}")
    print(f"Salário: {salario:.2f}")
    

     