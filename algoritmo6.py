#algoritmo que receba a temperatura em graus Celsius e apresente o valor convertido para graus Fahrenheit.
#Lê a temperatura em graus Celcius e converte para float
temp_celsius = float(input("Informe a temperatura em graus Ceulsius: "))
#Calcula a temperatura em graus Fahrenheit
temp_fahrenheit = (temp_celsius * 9/5) + 32
#Mostre o resultado da temperatura em graus Fahrenheit
print("A temperatura em graus Fahrenheit é: ", temp_fahrenheit)