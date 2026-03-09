
# Punto 4 – Comparación de rendimiento: C (compilado) vs Python (interpretado)

## Descripción
Se implementa la misma función recursiva de Fibonacci en C y en Python para comparar el rendimiento de un lenguaje compilado frente a uno interpretado.

## Archivos
- `fib.c`: Código en C.
- `fib.py`: Código en Python.

## Requisitos
- Compilador de C (gcc)
- Python 3

## Ejecución

### 1. Compilar y ejecutar el programa en C
```bash
gcc fib.c -o fib
./fib
```

### 2. Ejecutar el programa en Python
```bash
python3 fib.py
```

## Resultados obtenidos (en mi máquina)

| Lenguaje | n   | Tiempo (segundos) |
|----------|-----|-------------------|
| C        | 45  | 8.888425          |
| Python   | 45  | 205.719000        |

**Observación:** Python es aproximadamente **43 veces más lento** que C para este cálculo recursivo.

