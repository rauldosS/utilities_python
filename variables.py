# 💡 invert variable value

x = 10
y = 'Raul'

x, y = y, x

print(f'x={x} and y={y}')

# 💡 ternary operation

logged_user = False

message = 'User logged' if logged_user else 'User not logged' 

print(message)

# 💡 Conditional expression with OR
name = input('name: ')

print(name or "You didn't type your name")