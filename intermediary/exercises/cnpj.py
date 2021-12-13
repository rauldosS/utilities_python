'''
    04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

    0 4 2 5 2 0 1 1 0 0 0 1
    5 4 3 2 9 8 7 6 5 4 3 2
    0 16 6 10 18 0 7 6 0 0 0 2 = 65
    Formula -> 11 - (65% 11) = 1
    First digit = 1 (If the digit is greater than 9, it becomes 0)

    0 4 2 5 2 0 1 1 0 0 0 1 1 X
    6 5 4 3 2 9 8 7 6 5 4 3 2
    0 20 8 15 4 0 8 7 0 0 0 3 2 = 67
    Formula -> 11 - (67 % 11) = 10 (As the result is greater than 9, then it is 0)
    Second digit = 0

    New CNPJ + Digits = 04.252.011/0001-10
    Original CNPJ = 04.252.011/0001-10
    Valid

    Recap.
    543298765432 -> First digit
    6543298765432 -> Second digit
'''

from itertools import count

cnpj = '04.252.011/0001-10'

cnpj = list(int(i) for i in cnpj[0:15] if i.isdigit())

regressive_multiplication = list(range(5, 1, -1)) + list(range(9, 1, -1))

sum_cnpj = sum([value * regressive_multiplication[index] for index, value in enumerate(cnpj)])

print(sum_cnpj)

formula = 11 - (sum_cnpj % 11)

print(formula)

# --------------------------

regressive_multiplication = list(range(6, 1, -1)) + list(range(9, 1, -1))

print(regressive_multiplication)