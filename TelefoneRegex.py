import re

numeroRegex = re.compile(r'(\(\d\d\)) (\d\d\d\d\d\-\d\d\d\d)') # Os parenteses sem \ definem grupos.

mo = numeroRegex.search('(12) 98161-1177 (12) 98126-0585') # Acha só o primeiro.

print(mo.group()) # mo.group(1 ou 2) para achar o que escolher.

mo2 = numeroRegex.findall('(12) 98161-1177 (12) 98126-0585') # Acha todos.

print(mo2)