nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura (m): '))
peso = float(input('Digite seu peso (kg): '))

imc = peso / (altura ** 2)

print(f'Olá, {nome}, seu IMC é: {imc:.2f}')