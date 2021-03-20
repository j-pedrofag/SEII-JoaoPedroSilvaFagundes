#Print Welcome Message
print('Hello World')

#Criando uma variável com uma mensagem de texto

message = 'Hello World '
print(message)
#ou
m = 'Hello world'
print(m)
#ou 
my_message = 'Hello World'
print(my_message)

#Escrevendo textos com aspas simples no meio das palavras

exemplo1 = 'Bobby\'s World'
print(exemplo1)

#Escrevendo textos com aspas duplas

exemplo2 = "Bobby's World"
print(exemplo2)

#Escrevendo textos com quebra de linhas

exemplo3 = """Bobby's World 
was a good cartoon in the 1990s"""
print(exemplo3)

#Comando para descobrir o tamanho da string
print(len(message))

#Acessando os caracteres da string individualmente
print(message[0])

#Acessando intervalo de caracteres da string
print(message[0:5])

#Acessando intervalo de caracteres da string sem usar o começo e o fim
print(message[:5])
print(message[6: ])

#Comando para imprimir a mensagem em letras minúsculas 
print(message.lower())

#Comando para imprimir a mensagem em letras maiúsculas 
print(message.upper())

#Comando para contar a quantidade de uma determinada letra na mensagem
print(message.count('l'))

#Comando para achar o começo de uma palavra na string
print(message.find('World'))

#Comando para substituir uma palavra na string
new_message = message.replace('World', 'Universe')
print(new_message)

#Concatenando strings
greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name + '. Welcome!'
print(message)

#Simplicando a linha de concatenação 
message = '{}, {}, Welcome!'. format(greeting,name)
print(message)
#ou
message = f'{greeting}, {name.upper()}, Welcome!'
print(message)

#Comando para acessar o diretório das funções possíveis
print(dir(message))

#Comando de ajuda de parâmetros
print(help(str.lower))