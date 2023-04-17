funcao = 'Vendas = 2.9389 + 0.045765*TV + 0.18853*radio + -0.0010375*newspaper'
tv = 230.1
radio = 37.8
newspaper = 69.2

funcao = funcao.replace('TV', str(tv))
funcao = funcao.replace('radio', str(radio))
funcao = funcao.replace('newspaper', str(newspaper))

exec(funcao)
print(Vendas)