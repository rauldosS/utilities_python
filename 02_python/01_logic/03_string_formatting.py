"""
     String Formatting
"""

name = "Raul"
age = 21
imc = 10.4123123

print(f"{name} is {age} years old and its imc is {imc:.2f}")
print("{} is {} years old and its imc is {:.2f}".format(name, age, imc))
print("{a} is {b} years old and its imc is {c:.2f}".format(a=name, b=age, c=imc))