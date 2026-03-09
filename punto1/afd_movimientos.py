# punto1/afd_movimientos.py
import sys

class AFDMovimientos:
    def __init__(self):
        # Tabla de transiciones: estado -> {tipo_carácter: siguiente_estado}
        self.trans = {
            0: {'letra': 1},
            1: {'letra': 1, 'espacio': 2, '-': 3, 'X': 4},
            2: {'espacio': 2, '-': 3, 'X': 4},
            3: {'>': 5},
            4: {'espacio': 6, 'letra': 7},
            5: {'espacio': 6, 'letra': 7},
            6: {'espacio': 6, 'letra': 7},
            7: {'letra': 7, 'digito': 8},
            8: {}
        }
        self.aceptacion = {7, 8}

    def clasificar(self, c):
        if c.isalpha() and c.islower():
            return 'letra'
        elif c.isdigit():
            return 'digito'
        elif c.isspace():
            return 'espacio'
        elif c == '-':
            return '-'
        elif c == '>':
            return '>'
        elif c == 'X':
            return 'X'
        else:
            return None

    def acepta(self, cadena):
        estado = 0
        for c in cadena:
            tipo = self.clasificar(c)
            if tipo is None or tipo not in self.trans[estado]:
                return False
            estado = self.trans[estado][tipo]
        return estado in self.aceptacion

if __name__ == "__main__":
    afd = AFDMovimientos()
    archivo = "prueba.txt"
    try:
        with open(archivo, "r") as f:
            lineas = [linea.rstrip('\n') for linea in f]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
        sys.exit(1)

    for cadena in lineas:
        resultado = "ACEPTA" if afd.acepta(cadena) else "RECHAZA"
        print(f"'{cadena}': {resultado}")
