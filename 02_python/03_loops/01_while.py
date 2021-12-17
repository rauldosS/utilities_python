"""
    While this condition is true do:
    
    while condition:
        pass

	continue    - go to the next iteration
	break       - get out of the loop
"""
     
# While/Else - Accumulators
counter = 0
accumulator = 0
while counter <= 100:
    print(counter, accumulator)
    accumulator = accumulator + counter
    counter += 1
else:
    print('I arrived at else')
    
# While - Interacting Strings
phrase = 'The mouse has gnawed at the clothes of the king of rome'
counter = 0
phrase_length = len(phrase)

while counter < phrase_length:
    print(phrase[counter])
    
    counter += 1