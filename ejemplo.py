##Este ejercico usa las 2,3,10,14 reglas de zen de python
import math

# Explícito es mejor que implícito.
def calcular_area_circulo(radio):
    # Simple es mejor que complejo.
    area = math.pi * radio ** 2
    return area

# Los errores nunca deberían pasar en silencio, a menos que se silencien explícitamente.
def mostrar_area_circulo(radio):
    try:
        area = calcular_area_circulo(radio)
        print(f"El area del circulo con radio {radio} es: {area}")
    except TypeError:
        print("Error: El radio debe ser un número.")

# Ahora es mejor que nunca.
mostrar_area_circulo(5)