anoNascimento = int(input("Em que ano você nasceu? "))
anoAtual = int(input("Em que ano estamos? "))

idade = anoAtual - anoNascimento
idadeSemanas = idade * 48

print(f"A sua idade é: {idade}")
print(f"Sua idade em semanas é: {idadeSemanas}")