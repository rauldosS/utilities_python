# 💡 iterating string
text = 'Python'

for letter in text:
	print(letter)

for n, letter in enumerate(text):
	print(n, letter)

# 💡 range(start=0, stop, step=1)

for n in range(10):
	print(n)

for n in range(20, 10, -1):
	print(n)

# 💡 for / else
letters =   ['A', 'B', 'C', 'D', 'E']

for letter in letters:
    if letter == 'C':

        break
else:
    print('The letter "C" does not exist')

# continue 💡   - go to the next iteration
# break 💡      - get out of the loop