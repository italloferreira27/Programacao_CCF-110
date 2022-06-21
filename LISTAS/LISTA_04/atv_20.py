tempo = 0
massa = 0
m = float(input('Digite a massa em gramas:'))
while (m > 0.10):
  massa = m * 0.25
  tempo += 30
  m = m - massa
t = tempo/60
print(f"Gastou {t} minutos.")