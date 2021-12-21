"""
https://exchangeratesapi.io/
https://api.exchangeratesapi.io/latest
"""

dictionary_clients = {
    1: {
        'name': 'Luiz Otávio',
        'surname': 'Miranda',
        'age': 25,
        'height': 1.80,
        'weight': 80.53,
    },
    2: {
        'name': 'Maria',
        'surname': 'Oliveira',
        'age': 52,
        'height': 1.67,
        'weight': 57,
    },
    3: {
        'name': 'Pedro',
        'surname': 'Faria',
        'age': 32,
        'height': 1.95,
        'weight': 113,
    },
}

clients_json = """
{
    "1": {
        "name": "Luiz Ot\u00e1vio",
        "surname": "Miranda",
        "age": 25,
        "height": 1.8,
        "weight": 80.53
    },
    "2": {
        "name": "Maria",
        "surname": "Oliveira",
        "age": 52,
        "height": 1.67,
        "weight": 57
    },
    "3": {
        "name": "Pedro",
        "surname": "Faria",
        "age": 32,
        "height": 1.95,
        "weight": 113
    }
}
"""