peso = int(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en mt: "))
imc = peso / (estatura * estatura)
print(f"Tu indice de masa corporal es: {imc}")
print("---Rangos del IMC (adultos)---\n")

if imc <= 18.5:
    print("Bajo peso")
elif imc == 18.5 or imc <= 24.9:
    print(f"Peso normal (saludable)\n")
elif imc == 25.0 or imc <= 29.9:
    print(f"Sobrepeso\n")
elif imc == 30.0 or imc <= 34.9:
    print(f"Obesidad grado I\n")
elif imc == 35.0 or imc <= 39.9:
    print(f"Obesidad grado II\n")
elif imc >= 40.0:
    print(f"Obesidad grado III (obesidad mórbida)\n")
