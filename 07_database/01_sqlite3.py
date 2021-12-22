"""
    → SQLite3
"""

import sqlite3

conexao = sqlite3.connect('database.db')
cursor = conexao.cursor() # Possibilita executar comandos SQL

cursor.execute( 'CREATE TABLE IF NOT EXISTS clientes ('
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'nome TEXT,'
                    'peso REAL'
                ')')

""" INSERINDO
cursor.execute('INSERT INTO clientes (nome,peso) VALUES ("Raul Moraes", 85.3)')
cursor.execute('INSERT INTO clientes (nome,peso) VALUES ("André Roberto", 90.2)')
cursor.execute('INSERT INTO clientes (nome,peso) VALUES (?, ?)', ('Maria', 50))
cursor.execute(
    'INSERT INTO clientes (nome,peso) VALUES (:nome, :peso)',
    {'nome': 'Eduardo', 'peso': 99}
)
cursor.execute(
    'INSERT INTO clientes VALUES (:id, :nome, :peso)',
    {'id': None, 'nome': 'Daniel', 'peso': 105}
)
"""

conexao.commit()

"""
MANIPULANDO DADOS
"""

# UPDATE
cursor.execute(
    'UPDATE clientes SET nome=:nome WHERE id=:id',
    {'nome': 'Joana', 'id': 2}
)

# DELETE
cursor.execute(
    'DELETE FROM clientes WHERE id=:id',
    {'id': 1}
)

conexao.commit()

# SELECTS

cursor.execute('SELECT * FROM clientes')
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 60')

for linha in cursor.fetchall():
    nome, peso = linha

    print(nome, peso)



# Fechar tudo antes de finalizar a execução
cursor.close()
conexao.close()