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
listaNumeros = []
listaPares = []
for c in range(1, 5):
	listaNumeros.append(int(input(f"Digite  o {c}º número: ")))
    
def numerosPares(dividendos):
    for num in dividendos:
        if(num % 2 == 0):
            listaPares.append(num)
    print(listaPares)
    
numerosPares(listaNumeros)
