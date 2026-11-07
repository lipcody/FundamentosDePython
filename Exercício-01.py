idade = int(input("Digite sua idade: "))

# Procssamento

idadeEmMeses = idade * 12
idadeEmDias = idade * 365
idadeEmHoras = idadeEmDias * 24
idadeEmMinutos = idadeEmHoras * 60

print(f"Sua idade em meses: {idadeEmMeses}")
print(f"Sua idade em dias: {idadeEmDias}")
print(f"Sua idade em horas: {idadeEmHoras}")
print(f"Sua idade em minutos: {idadeEmMinutos}")
