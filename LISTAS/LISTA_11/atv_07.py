'''
7. Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere dois outros arquivos,
um contendo os endereços IP válidos e outro contendo os endereços inválidos. O formato de um endereço
IP é num1.num.num.num, onde num1 vai de 1 a 255 e num vai de 0 a 255.

IPs:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

https://www.youtube.com/watch?v=OP5cruGz8t4

'''


def ip_valido(ip_string):
    partes = ip_string.split('.')
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        parte_integer = int(parte)
        if parte_integer < 0 or parte_integer > 255:
            return False
    return True

nome_arquivo = input('Arquivo de IPs: ')
ips = open(nome_arquivo, "r")
lista_ips = ips.read().split("\n")
ips.close()

validos = []
invalidos = []

for ip in lista_ips:
    if ip_valido(ip) == True:
        validos.append(ip)
    else:
        invalidos.append(ip)

if len(validos) > 0 or len(invalidos) > 0:
    arquivo_valido = open("validos.txt", "w")
    arquivo_invalido = open("invalidos.txt", "w")
    
    if len(validos) > 0:
        for valido in validos:
            arquivo_valido.write(valido+"\n")

    if len(invalidos) > 0:
        for invalido in invalidos:
            arquivo_invalido.write(invalido+"\n")
    
    arquivo_valido.close()
    arquivo_invalido.close()
    print('Os Ips foram analizados!')
else:
    print("O arquivo de IPs está vazio")