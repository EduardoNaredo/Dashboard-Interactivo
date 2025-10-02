print("Este es un archivo que nos dará la bienvenida")

print("Hola, bienvenido a mi programa")

a = 89
b = 52
c = 23

def suma():
    print("La suma es:", a + b + c)

    suma()

def generar_datos_ventas():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    ventas = [120, 150, 200, 250, 300]
    return dias, ventas

def resumen_analitica():
    dias, ventas = generar_datos_ventas()
    total = sum(ventas)
    promedio = total / len(ventas)
    return {
        "dias": dias,
        "ventas": ventas,
        "total": total,
        "promedio": promedio
    }

datos = resumen_analitica()
print("Total de ventas:", datos["total"])
print("Promedio de ventas:", datos["promedio"])

