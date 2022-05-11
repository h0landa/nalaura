from cores import colorir


def alinhar(texto, val):
    return f"{texto: ^{val}}"

#usar text.center(valor da centalização)
def titulo(texto, cor='preto', fundo='preto'):
    return colorir(f"""
+ {(len(texto) * 3) *  '-'} +
{colorir(alinhar(texto,len(texto) * 3), cor)}
+ {(len(texto) * 3) *  '-'} +""", 'vermelho', 'branco')
txt = str(input('Digite seu texto: '))
color = str(input('Digite a cor: '))
fundo = str(input('Digite sua cor de fundo: '))
print(titulo(txt, color, fundo))
