#Operadores Logicos

#Programa para ver se pode entrar em um brinquedo de park
idade = 18
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)
msg = 'Pode entrar no brinquedo? ' + str(resultado)

print(msg)


# projeto de alarme

porta = 'f'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg2 = 'Alarme disparado? ' + str(alarme)
print(msg2)


#projeto de conta

tem_dinheiro = False
tem_dinheiro = not tem_dinheiro
msg3 = 'Tem dinheiro? ' + str(tem_dinheiro)
print(msg3)