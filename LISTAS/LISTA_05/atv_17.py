#EX. 17
nump = 1
while(nump != 0):
  nump = int(input('Digite o número do pedido:'))
  if(nump != 0):
    dd, mm, aa = map(int, input('Digite a data(dd/mm/aa): ').split("/"))
    precunit = float(input('Digite o preço unitário: R$'))
    quant = int(input('Digite a quantidade: '))
    print(f"Valor total da compra N°{nump} é de R${quant*precunit}")