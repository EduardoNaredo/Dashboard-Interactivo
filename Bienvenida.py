print("Este es un archivo que nos dará la bienvenida")

print("Hola, bienvenido a mi programa")

a = 89
b = 52
c = 23

def suma():
    print("La suma es:", a + b + c)

    suma()

import matplotlib.pyplot as plt

def graficar_ventas(dias, ventas):
    plt.figure(figsize=(8, 4))
    plt.plot(dias, ventas, marker='o', linestyle = "-", color = "blue")
    plt.title("Ventas Diarias")
    plt.xlabel("Días")
    plt.ylabel("Ventas")
    plt.grid(True)
    plt.show()

def main_frontend():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    ventas = [150, 200, 250, 300, 400]
    graficar_ventas(dias, ventas)

main_frontend()