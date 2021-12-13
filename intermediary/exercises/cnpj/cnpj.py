import re

REGRESSIVE = list(range(6, 1, -1)) + list(range(9, 1, -1))

def validate(cnpj):
    cnpj = onlyCnpj(cnpj)

    digit_1 = calculateDigit(cnpj[:-2], REGRESSIVE[1:])
    digit_2 = calculateDigit(cnpj[:-2] + str(digit_1), REGRESSIVE)

    return cnpj == f'{ cnpj[:-2] }{ digit_1 }{ digit_2}'

def onlyCnpj(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def calculateDigit(cnpj, regressive_multiplication):
    sum_digits = sum([int(value) * regressive_multiplication[index] for index, value in enumerate(cnpj)])

    result = 11 - (sum_digits % 11)
    result = 0 if result > 9 else result

    return result