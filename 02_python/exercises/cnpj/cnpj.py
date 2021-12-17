import re, random

REGRESSIVE = list(range(6, 1, -1)) + list(range(9, 1, -1))

def validate(cnpj):
    cnpj = onlyCnpj(cnpj)

    first_digit = calculateDigit(cnpj[:-2], REGRESSIVE[1:])
    second_digit = calculateDigit(cnpj[:-2] + str(first_digit), REGRESSIVE)

    return cnpj == f'{ cnpj[:-2] }{ first_digit }{ second_digit }'

def onlyCnpj(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def calculateDigit(cnpj, regressive_multiplication):
    sum_digits = sum([int(value) * regressive_multiplication[index] for index, value in enumerate(cnpj)])

    result = 11 - (sum_digits % 11)
    result = 0 if result > 9 else result

    return result

def generate():
    first_digit = random.randint(0, 9)
    second_digit = random.randint(0, 9)

    second_block = random.randint(100, 999)
    third_block = random.randint(100, 999)
    bedroom_block = '0001'

    initial_cnpj = f'{ first_digit }{ second_digit }{ second_block }{ third_block }{ bedroom_block }'

    first_digit_calcule = calculateDigit(initial_cnpj, REGRESSIVE[1:])
    second_digit_calcule = calculateDigit(initial_cnpj + str(first_digit_calcule), REGRESSIVE)

    new_cnpj = f'{ initial_cnpj }{ first_digit_calcule }{ second_digit_calcule }'

    return new_cnpj

def format(cnpj):
    cnpj = onlyCnpj(cnpj)

    formatted = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'

    return(formatted)