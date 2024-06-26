"""
Ahora mismo este codigo no funciona porque es imposible salir del while.
Debes:
 1. Ejecutar el programa y detectar el error.
 2. Corregir ese error para que salga del while
 3. Terminar el for de impresion para que imprima algo como esto
      0 entradas de BEBE: 0.00 €
      3 entradas de NIÑO: 42.00 €
      2 entradas de ADULTO: 46.00 €
      1 entradas de JUBILADO: 18.00 €
      -----------
      TOTAL: 96.00 €
 4. Corregir cualquier otro error que pueda haber, recuerda que no hemos probado nada
 --
 5. Opcional. Si eres capaz de que escriba entrada cuando solo sea una y entradas en otro caso... estaría muy bien.
"""

tipos_entrada = {
    "BEBE": {"EDAD": 3, "PRECIO": 0, "CONTADOR": 0},
    "NIÑO": {"EDAD": 13, "PRECIO": 14, "CONTADOR": 0},
    "ADULTO": {"EDAD": 65, "PRECIO": 23, "CONTADOR": 0},
    "JUBILADO": {"EDAD": float('inf'), "PRECIO": 18, "CONTADOR": 0}
}

edad = 0

while edad != '':

    edad = input("Edad: ")
    if edad == '':
        break

    edad = int(edad)

    if edad < 3:
        tipos_entrada["BEBE"]["CONTADOR"] = tipos_entrada["BEBE"]["CONTADOR"] + 1
    elif edad < 13:
        tipos_entrada["NIÑO"]["CONTADOR"] = tipos_entrada["NIÑO"]["CONTADOR"] + 1
    elif edad < 65:
        tipos_entrada["ADULTO"]["CONTADOR"] = tipos_entrada["ADULTO"]["CONTADOR"] + 1
    else:
        tipos_entrada["JUBILADO"]["CONTADOR"] = tipos_entrada["JUBILADO"]["CONTADOR"] + 1

total = 0
for tipo, valores in tipos_entrada.items():
    subtotal = valores['CONTADOR'] * valores['PRECIO']
    print(f"{valores['CONTADOR']} de {tipo}: {subtotal:.2f} Euros")
    total += subtotal

print(f"\nTotal Final: {total:.2f} Euros")
