i = int(input()) # Entrada da idade

# Calcular a idade em anos
ano = i//365
r = i%365

# Calcular a idade em mes
mes = r//30
d = r%30

print(ano,"ano(s)")
print(mes,"mes(es)")
print(d,"dia(s)")
