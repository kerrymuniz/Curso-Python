#Exercício 1 - Cálculo IMC (peso/altura**2)
nome = input("Digite seu nome: ")
peso = input("Digite seu peso(kg): ")
altura = input("Digite sua altura(m): ")
imc = float(peso) / float(altura)**2
    #esse f é de formatação de strings
if(imc >= 18.5 and imc <= 24.9):
    resultado = f'{nome} tem {float(altura):.2f} de altura, pesa {float(peso)}kg e seu Índice de Massa Corporal está normal.'
    print("Resultado: ",imc)
    print(resultado)
elif(imc < 18.5):
    resultado = f'{nome} tem {float(altura):.2f} de altura, pesa {float(peso)}kg e seu Índice de Massa Corporal está abaixo do normal.'
    print("Resultado: ",imc)
    print(resultado)
else:
    resultado = f'{nome} tem {float(altura):.2f} de altura, pesa {float(peso)}kg e seu Índice de Massa Corporal está elevado.'
    print("Resultado: ",imc)
    print(resultado)

#Exercício 2 - Retornar o maior nº numa lista de números
