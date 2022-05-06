
cores = [{'nome':'preto','cor': '\033[1;30m'}, {'nome':'vermelho','cor':'\033[1;31m'}, 
{'nome':'verde','cor':'\033[1;32m'},{'nome':'amarelo','cor':'\033[1;33m'}, {'nome':'azul','cor': '\033[1;34m'}, 
{'nome':'magenta','cor': '\033[1;35m'},{'nome':'cyan','cor':'\033[1;36m'}, {'nome':'cinza claro','cor':'\033[1;37m'},
{'nome':'cinza escuro','cor':'\033[1;90m'}, {'nome':'vermelho claro','cor':'\033[1;91m'}, 
{'nome':'amarelo claro','cor':'\033[1;93m'}, {'nome':'azul claro','cor':'\033[1;94m'}, {'nome':'magenta claro','cor':'\033[1;95m'}, 
{'nome':'cyan claro','cor':'\033[1;96m'}, 
{'nome':'branco','cor':'\033[1;97m'}]
cor = {}
def colorir(text, cor='preto', fundo='preto'):
    for c in cores:
        if cor == c['nome']:
            cor = c['cor'][:-1]
        if fundo == c['nome']:    
            fundo = c['cor'].split(';')
            fundo = fundo[1].replace('m','')
            fundo = int(fundo) + 10
            fundo =  ';' + str(fundo) + 'm'
    return(f'{cor + fundo + text}\033[m')


def doc():
    for e in range(0,7 + 1):
        for c in range(0,7):
            print(f'\033[1;3{e};10{c}mOlá,Mundo!\033[m',f'      033[1;3{e};10{c}mOlá,Mundo!033[m')
            print(f'\033[1;3{c};10{e}mOlá,Mundo!\033[m',f'      033[1;3{e};10{c}mOlá,Mundo!033[m')

