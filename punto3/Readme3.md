
# Punto 3 – Calculadora con raíz cuadrada (flex + bison)

## Descripción
Calculadora de expresiones aritméticas que soporta:
- Operadores: `+`, `-`, `*`, `/`
- Paréntesis
- Función `sqrt()` (raíz cuadrada) implementada con el método de Newton‑Raphson.
- Números enteros y decimales.
- Números negativos (operador unario `-`).

Lee expresiones desde un archivo de texto y muestra los resultados en consola.

## Archivos
- `calculadora.l`: Analizador léxico (flex).
- `calculadora.y`: Analizador sintáctico (bison) con la acción semántica y el método de Newton‑Raphson.
- `entrada.txt`: Archivo de ejemplo con expresiones (opcional).

## Requisitos
- `flex`
- `bison`
- `gcc`

## Compilación (manual)

### Paso 1: Generar el analizador léxico
```bash
flex calculadora.l
```
Esto crea el archivo `lex.yy.c`.

### Paso 2: Generar el analizador sintáctico
```bash
bison -d calculadora.y
```
Esto crea `calculadora.tab.c` y `calculadora.tab.h`.

### Paso 3: Compilar el ejecutable
```bash
gcc lex.yy.c calculadora.tab.c -o calculadora -lm
```

## Ejecución

### Con archivo de entrada
```bash
./calculadora entrada.txt
```

### Modo interactivo (sin archivo)
```bash
./calculadora
```
Escriba expresiones, una por línea. Termine con `Ctrl+D`.

## Ejemplo de entrada (entrada.txt)
```
2+3
sqrt(25)
(5+3)/2
sqrt(2)+1
sqrt(0)
sqrt(-4)
10/3
```

## Salida esperada
```
Resultado: 5.000000
Resultado: 5.000000
Resultado: 4.000000
Resultado: 2.414214
Resultado: 0.000000
Error: raíz cuadrada de número negativo
Resultado: 0.000000
Resultado: 3.333333
```


