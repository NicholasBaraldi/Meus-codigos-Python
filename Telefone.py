def telefone(numero): # (12) 98161-1177
	if len(numero) != 15:
		return False

	if numero[0] != '(':
		return False

	if numero[3] != ')':
		return False
	
	if numero[4] != ' ':
		return False
	
	if numero[10] == '-' or ' ':
		return True

	if numero[1:2].isdigit() and numero[5:9].isdigit() and numero[11:14].isdigit():
		return True

	return True


print('Deixe sua mensagem com seu numero de telefone no formato (XX) XXXXX-XXXX. Ligaremos de volta assim que possivel!')

mensagem = input()

acharNumero = False
for i in range(len(mensagem)):
	pedaço = mensagem[i:i+15]
	if telefone(pedaço):
		print('Numero de telefone encontrado: ' + pedaço)
		acharNumero = True
if not acharNumero:
	print('Não foi possivel achar nenhum numero de telefone, verifique se estão escritos da maneira correta.')