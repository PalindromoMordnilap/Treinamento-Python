'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o 
código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
'''

cod1, num1, val1 = input().split()
cod2, num2, val2 = input().split()

cod1 = int(cod1)
num1 = int(num1)
val1 = float(val1)

cod2 = int(cod2)
num2 = int(num2)
val2 = float(val2)


total = (num1 * val1) + (num2 * val2)

print("VALOR A PAGAR: R$ {:.2F}".format(total))