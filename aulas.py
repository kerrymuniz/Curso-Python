# o sep é um separador dos argumentos
#print(12, 34, sep="-")

# Tipos de dados no python
#string -> tudo o que está dentro de aspas, conjunto de caracteres
#print('Oi!')

#int -> números inteiros
#print(10)

#float -> números com casas decimais
#print(15.6)

#boolean -> valores true ou false
#print(10 == 10)
#print(10 == 11)


#Exercício variável
# nome = 'Kerry'
# sobrenome = 'Santos'
# idade = 19
# nasc = '26-03-2005'
# altura = 175
# maior_idade = idade >= 18


# print("Nome: ", nome)
# print("Sobrenome: ", sobrenome)
# print("Idade: ", idade)
# print("Ano de nascimento: ", nasc)
# print("Altura em CM: ", altura)
# print("É maior de idade? ", maior_idade)

#Operadores aritméticos
# adicao = 1 + 1
# print(adicao)

# subtracao = 3 - 2
# print(subtracao)

# mult = 4 * 4
# print(mult)

# divisao = 6/2
# print(divisao)

# exponenciacao = 2 ** 5
# print(exponenciacao)

# modulo = 50 % 3
# print(modulo)


#id dos elementos em python
# elemento1 = 'x'
# elemento2 = 'y'

# print(id(elemento1))
# print(id(elemento2))


#Estrutura de repetição
# condicao = True
# while(condicao):
#     nome = input("Qual seu nome: ")
    
#     if(nome == "sair"):
#         break

# print("Acabou")


#CRUD - Create, Read, Update, Delete
    #append - adiciona um item no final
    #insert - adiciona um item no índice escolhido
    #pop - remove item do final ou do índice escolhido
    #del - apaga um índice
    #clear - limpa a lista
    #extend - estende a lista
    #+ - concatena listas


#Desempacotamento + tuplas
nome1, nome2, nome3 = ["cadeira", "lápis", "mesa"] #desempacotando
print(nome2)
i1, *_ = ["cadeira", "lápis", "mesa"] #desempacotando + variável que não vai usar
print(i1)

tupla = "futebol", "basquete", "vôlei" #tupla
print(tupla[2])
print(tupla)


