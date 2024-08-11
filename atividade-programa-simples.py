# Recebendo informações do usuário:
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
# Calculo da idade:
diferenca = 100 - idade
# Exibindo mensagem:
print("Olá {}! Faltam {} anos para você completar 100 anos.".format(nome,diferenca))