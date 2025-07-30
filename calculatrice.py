# On demande les deux nombres
num1 = input("Saisissez un premier nombre : ")
num2 = input("Saisissez un deuxième nombre : ")

# Vérification et conversion
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Erreur : vous devez saisir des nombres.")
    exit()

# On demande l'opération
operation = input("Saisissez une opération (+, -, *, /) : ")

# On effectue le calcul
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 == 0:
        print("Erreur : division par zéro.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Erreur : opération non reconnue.")
