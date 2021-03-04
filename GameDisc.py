if message.content.startswith('!game'):
        author = message.author.mention
        
        numero = random.randint(1,20)

        await message.channel.send('Eae ' + str(author) + ' Já que vc quer jogar alguma coisa tente adivinhar o numero entre 1 e 20, que eu pensei. Você tem 10 chances!')

        #print('DEBUG: O numero secreto é:' + str(numero))

        input(message.content)

        tentativas = 1

        if  int(message.content) == numero:
            await message.channel.send('Parabéns ' + str(author) + '! Você acertou o numero em ' + str(tentativas) + ' tentativa!')
            input(message.content)

        while int(message.content) != numero:

            tentativas = tentativas + 1

            if int(message.content) > numero:
                await message.channel.send('Errado! Tente um numero menor.')
                input(message.content)

            if int(message.content) < numero:
                await message.channel.send('Errado! Tente um numero maior.')
                input(message.content)

            if tentativas == 10:
                await message.channel.send('Infelizmente vc não conseguiu! O numero era: ' + str(numero) + '.')
                break

            if int(message.content) == numero:
                await message.channel.send('Parabéns ' + str(author) + '! Você acertou o numero em ' + str(tentativas) + ' tentativas!')
                break
