a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print(type(a))
soma = a + b
subtracao = a - b 
multiplicacao = a * b 
divisao = a / b 
resto = a % b
resultado = ('Soma: {soma}. \nSubtracao: {subtracao}. '
      '\nMultiplicacao: {multiplicacao}.'
      '\nDivisão: {divisao}.'
      '\nResto: {resto}.'.format(soma=soma,
                                subtracao=subtracao,
                                resto=resto,
                                multiplicacao=multiplicacao,
                                divisao=divisao))
print(resultado)

#print('soma: ' + str(soma))
#print(subtracao)
#print(multiplicacao)
#print(int(divisao))
#print(divisao)
#print(resto)