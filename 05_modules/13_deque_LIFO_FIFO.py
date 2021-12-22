"""
    Pilhas e filas
    Pilha (stack) - LIFO - last in, first out.
        Exemplo: Pilha de livros que são adicionados um sobre o outro

    Fila (queue) - FIFO - first in, first out.
        Exemplo: Uma fila de banco (ou qualquer fila da vida real)
    
    Filas podem ter efeitos colaterais em desempenho, porque a cada item
    alterado, todo os índices serão modificados.
"""

# Exemplo de Pilha
livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')

livro_removido = livros.pop()

print(livro_removido)

# Exemplo de Fila
from collections import deque

fila = deque(maxlen=10)

fila.append('Raul')
fila.append('Lucas')
fila.append('André')
fila.append('Samuel')

fila.popleft()
fila.pop()

fila.insert(2, 'Luiz') # Escolhe índice para adicionar
fila.index('Lucas') # Qual o índice do elemento