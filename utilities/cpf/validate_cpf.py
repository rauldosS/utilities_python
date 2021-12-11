"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

# Infinite loop
while True:
    # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    new_cpf = cpf[:-2]                  # Eliminates the last two digits of the CPF
    reverse = 10                        # reverse counter
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # First index goes from 0 to 9,
            index -= 9                  # These are the first 9 digits of the CPF

        total += int(new_cpf[index]) * reverse  # Total amount of multiplication

        reverse -= 1                    # Decreases the reverse counter
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:                   # If the digit is > 9 the value is 0
                d = 0
            total = 0                   # reset the total
            new_cpf += str(d)           # Concatenate the digit generated in the new CPF

    # Avoid sequels. E.g.: 11111111111, 00000000000...
    sequence = new_cpf == str(new_cpf[0]) * len(cpf)

    # I found that strings evaluated to true, so too
    # I added a check here
    if cpf == new_cpf and not sequence:
        print('Valid')
    else:
        print('Invalid')
