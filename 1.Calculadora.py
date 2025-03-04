def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

num1 = float(input("Ingresa el primer numero: "))
operacion = input("Elige 'suma' o 'resta': ").lower()
num2 = float(input("Ingresa el segundo numero: "))

if operacion == "suma":
    print(f"Resultado: {suma(num1, num2)}")
elif operacion == "resta":
    print(f"Resultado: {resta(num1, num2)}")
else:
    print("Operacion no valida.")