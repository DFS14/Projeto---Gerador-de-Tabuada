
#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Programa que gera a tabuada do número digitado


numero = int(input("Digite um número para gerar a tabuada: "))

print(f"Tabuada do {numero}:")

for valor in range(1, 11):
    resultado = numero * valor
    print(f"{numero} x {valor} = {resultado}")