from itertools import groupby, tee

students = [
    {'name': 'Luiz', 'note': 'A'},
    {'name': 'Letícia', 'note': 'B'},
    {'name': 'Fabrício', 'note': 'A'},
    {'name': 'Rosemary', 'note': 'C'},
    {'name': 'Joan', 'note': 'D'},
    {'name': 'John', 'note': 'A'},
    {'name': 'Eduardo', 'note': 'B'},
    {'name': 'André', 'note': 'C'},
    {'name': 'Anderson', 'note': 'B'},
]

sort = lambda item: item['note']

def orders(item):
    return item['note']

students.sort(key=sort)

grouped_students = groupby(students, sort)

# No tee (with list)
for grouping, grouped_values in grouped_students:
    values = list(grouped_values)
    print(f'Grouping: { grouping }')
    
    for student in values:
        print(f'\t{ student }')
        
    quantity = len(values)

    print(f'\t{ quantity } students scored { grouping }')


# with tee
for grouping, grouped_values in grouped_students:
    v1, v2 = tee(grouped_values)

    print(f'Grouping: { grouping }')

    for student in v1:
        print(f'\t{ student }')

    quantity = len(list(v2))
    print(f'\t{ quantity } students scored { grouping }')