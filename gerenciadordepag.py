print('-=-=-=-' * 5)
print('=-=-=LOJA DE ELETRODOMESTICOS=-=-=')

preço = int(input('digite o preço da compra: '))

print('FORMAS DE PAGAMENTO: ')
print('''[1] pagamento à vista com dinheiro/cheque
[2] à vista no cartão 
[3] 2x no cartão
[4] 3x ou mais no cartão''')

pagamento = int(input('Digite a forma de pagamento: '))

if pagamento == 1:
    #Quem pagou com dinheiro ou cheque ganha 10% de desconto#
    desconto = preço - (preço * 10/100)
    print('Sua compra de R${} à vista com dinheiro/cheque, ficou com desconto de 10% você pagara R${}'.format((preço),(desconto)))

elif pagamento == 2:
    #Quem pagou à vista no cartão ganha 5% de desconto#
    #des5 representa o desconto de 5%#
    des5 = preço - (preço * 5/100 )
    print('Sua compra de R$ {} à vista no cartão, ficou com desconto de 5%, ficando R${}'.format((preço), (des5)))

elif pagamento == 3:
    #Quem pagou em 2x no cartão não terá juros ou promoção#
    #v2 representa valor dividido em 2x# 
    v2 = preço / 2
    print('Sua compra de R${}, será em 2x no cartão sem juros ficará R${:.2f}'.format((preço), (v2)))

elif pagamento == 4:
    #Para o usuario que optou pela opção 4 irá digitar em quantas vezes ele vai dividir, e consequentemento terá juros de 20%# 
    opçao = int(input('Digite em quantas você quer dividir: '))
    #Valorcj representa o valor com juros# 
    valorcj = preço + (preço * 20/100 )
    v = valorcj / opçao
    print('Sua compra parcelada com juros de 20%, ficara R${}, dividido em {}x ficara R${}  '.format((valorcj), (opçao), (v)))




