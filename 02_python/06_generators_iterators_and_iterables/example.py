'''
    → Generators, unlike lists, do not allocate all values in memory.
    → It will return the value only when requested.

    → Lists, tuples and str → Sequences → Iterables
        → FOR loop → next()

    → Generators → iter()
        → 
'''

"""
for lê algo que chamamos de "iterável" (do inglês iterable)... Um iterável é algo que você pode percorrer 
(geralmente tem índices, como a string - ou não, como generators)... O que o for faz é solicitar ao iterador 
(que vamos aprender mais pra frente) da string: "Ei string, você tem um próximo valor?", e a string responde 
-> "Sim, aqui está" (letra) ou "Não, erro -> StopIteration".

O que "letra" é nesse código, é o valor que a string entrega na parte do "Sim". Isso ocorre repetidas vezes 
até o iterável (a string) falar que não tem mais valores. Nesse caso seu iterador (que vamos ver pra frente) 
vai levantar um erro (literalmente). Ao chegar na letra "a" final (de roma) o for vai solicitar mais um valor 
para a string. Nesse momento, como eles já acabaram, ela lança um erro chamado de StopIteration.

O for é programado, pelos desenvolvedores do Python, para capturar esse erro e parar as solicitações. 
Por esse motivo, nós não vemos erro e o for termina o código (do contrário isso se tornaria um loop infinito).

A parte mais legal disso tudo, é que enquanto o for solicita o valor e recebe de volta algo da string (uma letra), 
ele nos permite fazer algo com esse valor. Por exemplo, você fez "print(letra)", mas poderia ser qualquer outra coisa.

Perdoe se a resposta soou um tanto técnica, mas é que eu quero deixar essa pergunta como "melhores perguntas", 
porque ela ocorre bastante por aqui. Espero ter entendido =)
"""


numbers = list(range(10))

# Iterables
print(hasattr(numbers, '__iter__'))

# Iterators 
numbers = iter(numbers)
print(hasattr(numbers, '__next__'))

print(next(numbers)) # 0
print(next(numbers)) # 1
print(next(numbers)) # 2

# bytes consumed
import sys

numbers = list(range(1000000))

print(f'{ sys.getsizeof(numbers) } bytes')

# Generator range
def generate_range():
    for n in range(100):
        yield n

g = generate_range()

for v in g:
    print(v)

# Generator variable
def generate_variable():
    variable = 'value 1'
    yield variable

    variable = 'value 2'
    yield variable

    variable = 'value 3'
    yield variable

g = generate_variable()

print(next(g)) # value 1
print(next(g)) # value 2
print(next(g)) # value 3

# Compare
numbers_list = [x for x in range(1000)]
numbers_generator = (x for x in range(1000))

print(f'{ sys.getsizeof(numbers_list) } bytes ({ type(numbers_list) })')
print(f'{ sys.getsizeof(numbers_generator) } bytes ({ type(numbers_generator) })')

##############################
# Behavior Iterator and generator
name = 'Raul dos Santos Moraes'
iterator = iter(name)
generator = (letter for letter in name)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# FOR LOOP will display the rest of the iterations
print('Other itens')
for letter in generator:
    print(letter)

# Behavior Iterable
'''
    'When using them as iterators they will be converted to runtime and consumed.
'''