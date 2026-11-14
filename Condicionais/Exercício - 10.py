print("")
print("")
print("========================================================================")
print("Controle de margem de lucro")
print("========================================================================")
print("")

preco_custo = float(input("   Digite o preço de custo do produto: "))
percentual_lucro = float(input("   Digite o percentual de lucro desejado: "))

if percentual_lucro < 50:
    print("")
    print("=======================================================================")
    print("")
    print("(!) O produto será vendido com uma margem muito pequena de lucro.(!)")
    print("")
    print("=======================================================================")
    print("")
    
else:
    print("")
    print("=======================================================================")
    print("")
    preco_venda = preco_custo + (preco_custo * percentual_lucro / 100)
    print(f"O preço de venda do produto será: R$ {preco_venda:.2f}")
    print("")
    print("=======================================================================")