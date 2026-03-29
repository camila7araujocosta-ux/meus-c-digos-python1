#Algoritmo que receba a altura e o peso de uma pessoa e calcule o IMC
#Lê a altura
altura = float(input("Informe a altura: "))
#Lê o peso em Kg 
peso = float(input("Informe o peso em Kg: "))
#Calcule o IMC
IMC = peso / altura **2
#Mostre o resultado do IMC
print("O resultdado do IMC é: ", IMC)