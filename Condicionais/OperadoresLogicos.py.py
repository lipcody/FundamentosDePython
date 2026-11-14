idade = int(input("Digite sua idade: "))
ingresso = (input("Você tem ingresso? (s/n): "))

if not(idade >= 18 and ingresso == "s"):
    print("Você pode entrar no show.")
else:
    print("Você não pode entrar no show.")  
