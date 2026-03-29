#algoritmo que receba o valor de um produto e calcule o preço final considerando um acréscimo de 8% de imposto.
#Lê o valor do produto e converte para float
valor = float(input("Informe um valor: "))
#Calcula o preço final com acréscimo de 8% de imposto
preco_final= valor * 1.08 or valor + (valor * 0.08)
#Mostre o resultado do preço final
print("O preço final do produto é de: ", preco_final)