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
nome = input("\nDigite seu nome : ")
idade = input("Digite a sua idade: ")

if(nome != "" and idade != ""):
    print(f"\nSeu nome é {nome} e você tem {idade} anos")
    print(f"Seu nome invertido é {nome[::-1]}")
    
    if ' ' in nome:
        print("Seu nome CONTÉM espaços")
    else:
        print("Seu nome NÃO contém espaços")

    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é '{nome[0]}'")
    print(f"A última letra do seu nome é '{nome[4]}'")
else:
    print("Desculpe, você deixou campos vazios.")