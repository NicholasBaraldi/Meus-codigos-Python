### upper/lower:

frase = 'Olá Mundo!'

print(frase)

print(frase.upper())

frase = frase.upper()

print(frase)

frase = frase.lower()

print(frase)

#exemplo:

resposta = 'SIM' #o correto é um input(), coloquei o 'SIM' para facilitar.

#if resposta == 'sim':
#	print('starting')
## nesse caso, se a resposta for SIM o programa não reconhece.

if resposta.lower() == 'sim':
	print('starting')
#nesse caso tanto faz como a resposta é digitada, porque sera tranformada em minuscula.




### isupper/islower:

frase = 'Olá Mundo!'

print(frase.islower())

frase = 'olá mundo!'

print(frase.islower())

frase = 'OLÁ MUNDO!'

print(frase.isupper())

print('teste'.upper().isupper()) #retorna True.




### more string methods:

#isalpha() #Só letras.

#isalnum() #Só letras e numeros.

#isdecimal() #Só numeros.

#isspace() #Só espaço em branco.

#isttile() #Só titulo (palavras començando com maiusculas)

print('esse é o titulo do meu texto'.title())




### startswith/endswith:

print('ola mundo'.startswith('o'))

print('ola mundo'.endswith('o'))




### join/split:

print(', '.join(['gato', 'rato', 'cachorro']))

print('\n'.join(['gato', 'rato', 'cachorro']))

print('meu nome é nicholas'.split())

print('meu nome é nicholas'.split('e'))




### rjust/ljust/center

print('ola'.rjust(10))

print('ola'.ljust(10, '*'))

print('ola'.center(20, '-'))




### strip/rstrip/lstrip:

teste = 'oi'.rjust(10)

print(teste)

print(teste.strip()) #isso não remove definitivamente os espaços, só nesse print, para remover tem q ser: teste = teste.strip().

#strip('*') tbm funciona, da mesma forma q rstrip() e lstrip().

print('GatoGatoCachorroGatoPardalGatoGato'.strip('otaG')) #diferente do just, o strip funciona com palavras.




### replace:

teste = 'ola joao'

print(teste.replace('o', 'Z'))




# pyperclip

import pyperclip

pyperclip.copy('OLA!!!!!!!!!!!')

print(pyperclip.paste())