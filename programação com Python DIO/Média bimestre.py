a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre'))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Segundo bimestre'))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre'))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Quarto bimestre'))
media = (a + b + c + d) / 4
print('media: {}' .format(media))