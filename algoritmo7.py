#algoritmo que receba a quantidade de horas trabalhadas por um funcionário e o valor da hora trabalhada, calculando o salário total.
#Lê a quantidade de horas trabalhadas e converte parafloat
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas: "))
#Lê o valor da hora trabalhada e converte para float
valor_hora = float(input("Informe o valor da hora trabalhada: "))
#Calcula o salário total
salario_total = horas_trabalhadas * valor_hora
#Mostre o resultado do salário total
print("O salário total é:", salario_total)