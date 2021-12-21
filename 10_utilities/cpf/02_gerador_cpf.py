from random import randint
number = str(randint(100000000, 999999999))

new_cpf = number                    # 9 random numbers
reverse = 10                        # counter reverse
total = 0                           # The total of the multiplications

# Loop do CPF
for index in range(19):
    if index > 8:                   # First index goes from 0 to 9
        index -= 9                  # These are the first 9 digits of the CPF

    total += int(new_cpf[index]) * reverse  # Total amount of multiplication

    reverse -= 1                    # Decrements the counter reverse
    if reverse < 2:
        reverse = 11
        d = 11 - (total % 11)

        if d > 9:                   # If the digit is > 9 the value is 0
            d = 0
        total = 0                   # reset the total
        new_cpf += str(d)           # Concatenate the digit generated in the new CPF

print(new_cpf)