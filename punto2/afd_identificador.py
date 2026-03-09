# punto2/afd_identificador.py
import sys

class AFDIdentificador:
    def __init__(self):
        # Tabla de transiciones: estado -> {tipo_carácter: siguiente_estado}
        self.trans = {
            0: {'letra': 1},
            1: {'letra': 1, 'digito': 1}
        }
        self.aceptacion = {1}

    def clasificar(self, c):
        if c.isalpha():  # mayúsculas o minúsculas
            return 'letra'
        elif c.isdigit():
            return 'digito'
        else:
            return None

    def acepta(self, cadena):
        if not cadena:  # cadena vacía
            return False
        estado = 0
        for c in cadena:
            tipo = self.clasificar(c)
            if tipo is None or tipo not in self.trans[estado]:
                return False
            estado = self.trans[estado][tipo]
        return estado in self.aceptacion

if __name__ == "__main__":
    afd = AFDIdentificador()
    archivo = "prueba.txt"
    try:
        with open(archivo, "r") as f:
            lineas = [linea.rstrip('\n') for linea in f]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
        sys.exit(1)

    print("Pruebas de identificadores:")
    for cadena in lineas:
        resultado = "ACEPTA" if afd.acepta(cadena) else "NO ACEPTA"
        print(f"'{cadena}': {resultado}")
