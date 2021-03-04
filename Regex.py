import re

batRegex = re.compile(r'Bat(wo)?man') #?: 0 ou 1/ *: 0 ou mais/ +: 1 ou mais/ {x}: o numero de vezes que vc quiser/ {x, y}: minimo e maximo.
mo = batRegex.search('as aventuras do Batwoman Batman Batman Batwoman')
mo.group()