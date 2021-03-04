import pprint #serve para deixar o print bonito, em ordem alfabetica.

message = 'Remember remember the fifth of november.'
count = {} 

for character in message.upper(): #.upper serve para deixar tudo maisculo e não contar minusculas e maiusculas separado.
	count.setdefault(character, 0)
	count[character] = count[character] + 1

pprint.pprint(count)