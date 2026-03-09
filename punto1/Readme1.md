# Punto 1 – AFD para movimientos de ajedrez (notación descriptiva)

## Descripción
Implementación de un Autómata Finito Determinista (AFD) que reconoce movimientos de ajedrez en notación descriptiva según la expresión regular:

`[kq]?[bnr]?[prnbkq] ('->'|'X') [kq]?[bnr]?[prnbkq] [1-8]?`

**Ejemplos válidos:** `p->k4`, `kbp X qn`, `kbpXqn`, `rXq`

## Archivos
- `afd_movimientos.py`: Clase AFD y programa principal.
- `prueba.txt`: Archivo con casos de prueba (uno por línea).

## Requisitos
- Python 3.8 o superior.

## Ejecución
```bash
python3 afd_movimientos.py
