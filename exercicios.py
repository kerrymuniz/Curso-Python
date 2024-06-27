#Exercício 1 - Cálculo IMC (peso/altura**2)
# nome = input("Digite seu nome: ")
# peso = input("Digite seu peso(kg): ")
# altura = input("Digite sua altura(m): ")
# imc = float(peso) / float(altura)**2
#     #esse f é de formatação de strings
# if(imc >= 18.5 and imc <= 24.9):
#     resultado = f'{nome} tem {float(altura):.2f} de altura, pesa {float(peso)}kg e seu Índice de Massa Corporal está normal.'
#     print("Resultado: ",imc)
#     print(resultado)
# elif(imc < 18.5):
#     resultado = f'{nome} tem {float(altura):.2f} de altura, pesa {float(peso)}kg e seu Índice de Massa Corporal está abaixo do normal.'
#     print("Resultado: ",imc)
#     print(resultado)
# else:
#     resultado = f'{nome} tem {float(altura):.2f} de altura, pesa {float(peso)}kg e seu Índice de Massa Corporal está elevado.'
#     print("Resultado: ",imc)
#     print(resultado)


#Exercício 2 - Retornar o maior nº de uma lista de números
# def maiorNumero(a, b):
#     if(a > b):
#         return a
#     else:
#         return b
    
# def listaNumeros(lista):
#     maior_numero = 0
#     for numero in lista:
#         maior_numero = maiorNumero(maior_numero, numero)
#     return maior_numero

# lista_numeros = [0, 5, 15, 34, 7, 46, 55, 23, 75]
# print("Os números da lista são", 0, 5, 15, 34, 7, 46, 55, 23, "e", 75)
# print("O maior número da lista é", listaNumeros(lista_numeros))


#Exercício 3 - Função que retorna uma lista de números pares da lista de entrada
# listaNumeros = []
# listaPares = []
# for c in range(1, 5):
# 	listaNumeros.append(int(input(f"Digite  o {c}º número: ")))
    
# def numerosPares(dividendos):
#     for num in dividendos:
#         if(num % 2 == 0):
#             listaPares.append(num)
#     print("Os números pares da lista são", listaPares)
    
# numerosPares(listaNumeros)


#Exercício 4 - Interpolação de string % calcular salario do funcionário depois de + 5%
# nome = "O funcionário Kerry "
# salario_atual = input("Qual o salário atual? R$")
# salario_novo = float(salario_atual) + (float(salario_atual) * 5/100)

# print("Novo Ajuste:")
# variavel = '%s teve um ajuste em seu salário, com aumento de 5%, ficando em método de pagamento mensal %f' % (nome, str(salario_novo))
# print(variavel)


#Exercício 5 - função que recebe duas listas de inteiros e retorne os elementos em comum
# lista_int1 = []
# lista_int2 = []
# def intersecao(lista1, lista2):
#     #recuperando inteiros da 1ª lista
#     for num_lista1 in lista1:
#         if(num_lista1 >= 0):
#             lista_int1.append(num_lista1)
#     #recuperando inteiros da 2ª lista
#     for num_lista2 in lista2:
#         if(num_lista2 >=0):
#             lista_int2.append(num_lista2)
#     print("Primeira lista:", lista_int1)
#     print("Segunda lista:", lista_int2)

# lista_A = [2, 5, 7, 18, 34, 56, 114]
# lista_B = [18, 43, 56, 89, 95, 107, 7]
# inteirosComuns = [comum for comum in lista_A if comum in lista_B]
# intersecao(lista_A, lista_B)
# print("Os elementos em comum são", inteirosComuns)


#Exercício 6 - exercício para praticar função len e caracteres
# nome = input("\nDigite seu nome : ")
# idade = input("Digite a sua idade: ")

# if(nome != "" and idade != ""):
#     print(f"\nSeu nome é {nome} e você tem {idade} anos")
#     print(f"Seu nome invertido é {nome[::-1]}")
    
#     if ' ' in nome:
#         print("Seu nome CONTÉM espaços")
#     else:
#         print("Seu nome NÃO contém espaços")

#     print(f"Seu nome tem {len(nome)} letras")
#     print(f"A primeira letra do seu nome é '{nome[0]}'")
#     print(f"A última letra do seu nome é '{nome[4]}'")
# else:
#     print("Desculpe, você deixou campos vazios.")


#Exercício 7 - Try except
# try:
#     num1 = input("Digite o 1ª número: ")
#     num2 = input("Digite o 2ª número: ")
#     if(num1 != 0 and num2 != 0):
#         calculo = float(num1)/float(num2)
#         print(f"Divisão entre os números {num1} e {num2} = {calculo:.2f}")

# except:
#     print('Não foi possível realizar a operação por 0.')


#Exercício 8 - par ou ímpar
# numero = input("Digite um número inteiro: ")
# numeroInt = int(numero)
# par = numeroInt % 2
# if(numero.isdigit()):
#     if(par == 0):
#         print("O número digitado é par.")
#     else:
#         print("O número digitado é ímpar.")
# else:
#     print("O número digitado não é inteiro.")


#Exercício 9 - hora perguntada
# hora = input("Que horas são : ")
# horas = int(hora)
# if(horas >= 0 and horas <= 11):
#     print("Bom dia!")
# elif(horas >= 12 and horas <= 17):
#     print("Boa tarde!")
# else:
#     print("Boa noite!")


#Exercício 10 - tamanho nome usuário
# nome = input("Digite seu primeiro nome: ")
# if(len(nome) <= 4):
#     print("Seu nome é curto!")
# elif(len(nome) >= 5 and len(nome) <= 6):
#     print("Seu nome é normal!")
# else:
#     print("Seu nome é muito grande!")

#Exercíco 11 - salário final + comissão sobre total de vendas
# comissao = 0.05
# totalVendas = input("Digite o total de vendas realizadas: ")
# salarioFixo = input("Digite seu salário fixo: R$")
# calculo = float(salarioFixo) + (float(totalVendas) * comissao)
# print(f"Seu salário final é de R${calculo}")


#Exercício 12 - while
# nome = 'Kerry Muniz'
# indice = 0

# while(indice < len(nome)):
#     print(nome[indice])
#     indice += 1


#Exercício 13 - palavra secreta
# import os

# palavra_secreta = 'cadeira'
# letras_acertadas = ''
# tentativas = 0

# while True:
#     letra = input("Digite uma letra: ")
#     tentativas += 1

#     if len(letra) > 1:
#         print("Digite apenas uma letra.")
#     if letra.isdigit():
#         print("Digite apenas letras.")
    
#     if letra in palavra_secreta:
#         letras_acertadas += letra

#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'
#     print(palavra_formada)
#     if palavra_formada == palavra_secreta:
#         #os.system('clear')
#         print("PARABÉNS, VOCÊ ACERTOU!!")
#         print(f"A PALAVRA CORRETA É {palavra_secreta}")
#         print(f"VOCÊ PRECISOU DE {tentativas} TENTATIVAS PARA ACERTAR!")
#         letras_acertadas = ''
#         tentativas = 0


#Exercício 14 - exibir índices da lista
# lista = ["maçã", "laranja", "kiwi"]
# lista.append("limão")
# indices = range(len(lista))

# for i in indices:
#     print(i, lista[i])


#Exercício 15 - lista de compras
# import os

# lista = [] #declaração da lista vazia fora do while

# while True:
    
#     opcao = input("Selecione uma opção \n [i]nserir [a]pagar [l]istar: ")
    
#     if opcao == 'i':
#         os.system('cls')
#         valor_digitado = input("Valor: ")
#         lista.append(valor_digitado)
#     elif opcao == 'a':
#         os.system('cls')

#         indice_str = input("Escolha o índice para apagar: ")

#         try:
#             indice = int(indice_str)
#             del lista[indice]
#         except ValueError:
#             print("Por favor digitar apenas números inteiros.")
#         except IndexError:
#             print("Índice não existente na lista.")
#     elif opcao == 'l':
#         os.system('cls')

#         if len(lista) == 0:
#                 print('Não há itens na lista')
#         else:
#             for indice, item in enumerate(lista):
#                 print(indice, item)
#     else:
#         print("Por favor, escolha i, a ou l.")


#Exercício 16 - gerar primeiro e segundo digito de um CPF
# cpf = [7, 4, 6, 8, 2, 4, 8, 9, 0, 7, 0]
# nove_digitos = cpf[:9]
# contador = 10

# resultado = 0
# for cadaNum in nove_digitos:
#     print(f"{cadaNum} * {contador} = {cadaNum * contador}")
#     resultado += cadaNum * contador
#     contador -= 1
# print("Soma dos resultados:", resultado)
# resultado *= 10
# print("Multiplicação por 10:", resultado)
# resultado %= 11
# print("Resto da divisão do resultado por 11:", resultado)
# if(resultado > 9):
#     resultado = 0
#     print(f"Resultado é {resultado}")
# else:
#     resultado = resultado
#     print(f"Valor do primeiro dígito do CPF é {resultado}")
# #############################################################
# resultado_primeiro_digito = [resultado]
# dez_digitos = cpf[:9] + resultado_primeiro_digito
# print(dez_digitos)
# contador1 = 11
# resultado1 = 0

# for cadaNum in dez_digitos:
#     print(f"{cadaNum} * {contador1} = {cadaNum * contador1}")
#     resultado1 += cadaNum * contador1
#     contador1 -= 1
# print("Soma dos resultados:", resultado1)
# resultado1 *= 10
# print("Multiplicação por 10:", resultado1)
# resultado1 %= 11
# print("Resto da divisão do resultado por 11:", resultado1)
# if(resultado1 > 9):
#     resultado1 = 0
#     print(f"Resultado é {resultado1}")
# else:
#     resultado1 = resultado1
#     print(f"Valor do segundo dígito do CPF é {resultado1}")


#Exercício 17 - funções + *args
def multiplica(*args):
    total = 1
    for num in args:
        total *= num
    return total
    
print(multiplica(1, 2, 3, 4, 5, 2, 5))

def parImpar(x):
    if(x % 2 == 0):
        par = print(f"{x} é par.")
        return par
    else:
        impar = print(f"{x} é ímpar.")
        return impar
    
parImpar(8237)
