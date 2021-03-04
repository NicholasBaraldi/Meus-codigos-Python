import random

print('Qual seu nome?')

nome = input()

numero = random.randint(1,20)

print('Olá ' + nome + '! Eu pensei em um numero entre 1 e 20, tente adivinhar. Você tem 10 chances!')

#print('DEBUG: O numero secreto é:' + str(numero))

guess = input()

tentativas = 1

if  int(guess) == numero:
		print('Parabéns ' + nome + '! Você acertou o numero em ' + str(tentativas) + ' tentativa!')

while int(guess) != numero:

	tentativas = tentativas + 1

	if int(guess) > numero:
		print('Errado! Tente um numero menor.')
		guess = input()

	if int(guess) < numero:
		print('Errado! Tente um numero maior.')
		guess = input()

	if tentativas == 10:
		print('Infelizmente vc não conseguiu =( \nO numero era: ' + str(numero) + '.')
		break

	if int(guess) == numero:
		print('Parabéns ' + nome + '! Você acertou o numero em ' + str(tentativas) + ' tentativas!')
		break