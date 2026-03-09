

##  **README punto5 (corregido - sin requirements.txt)**

# Punto 5 – Calculadora de Fibonacci con ANTLR (Python)

## Descripción
Programa que reconoce el comando `FIBO(n)` y genera la serie de Fibonacci hasta el número `n` inclusive, utilizando un parser generado con ANTLR4.

Ejemplo:  
Entrada: `FIBO(20)`  
Salida: `0, 1, 1, 2, 3, 5, 8, 13`

## Archivos
- `Fibonacci.g4`: Gramática de ANTLR.
- `eval_fibo.py`: Programa principal con el visitor que calcula la serie.
- `FibonacciLexer.py`, `FibonacciParser.py`, `FibonacciVisitor.py`: Archivos generados por ANTLR (incluidos para facilitar la ejecución).

## Requisitos
- Python 3.8 o superior.
- Entorno virtual (recomendado).

## Instalación y ejecución

### 1. Crear y activar un entorno virtual
```bash
python3 -m venv antlr-env
source antlr-env/bin/activate   # En Linux/Mac
# En Windows: antlr-env\Scripts\activate
```

### 2. Instalar el runtime de ANTLR para Python
```bash
pip install antlr4-python3-runtime
```

### 3. Ejecutar el programa
```bash
python eval_fibo.py
```
Luego ingresa el comando, por ejemplo:
```
FIBO(20)
```

## Salida esperada
```
Ingrese el comando (ej: FIBO(20)):
FIBO(20)

Resultado: 0, 1, 1, 2, 3, 5, 8, 13
```

