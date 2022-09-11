n = int(input())
v1 = n // 100
v2 = (n % 100) // 50
v3 = ((n % 100) % 50) // 20
v4 = (((n % 100) % 50) % 20) // 10
v5 = ((((n % 100) % 50) % 20) % 10) // 5
v6 = (((((n % 100) % 50) % 20) % 10) % 5) // 2
v7 = ((((((n % 100) % 50) % 20) % 10) % 5) % 2) // 1
print(n)
print(v1, 'nota(s) de R$ 100,00')
print(v2, 'nota(s) de R$ 50,00')
print(v3, 'nota(s) de R$ 20,00')
print(v4, 'nota(s) de R$ 10,00')
print(v5, 'nota(s) de R$ 5,00')
print(v6, 'nota(s) de R$ 2,00')
print(v7, 'nota(s) de R$ 1,00')