

## Parcial 1 Brayan Camilo Moreno Cordero
Este repositorio contiene la solución a los 5 puntos del parcial de Lenguajes de Programación y Traducción. Cada punto está en su propia carpeta con los archivos necesarios y un README específico con instrucciones detalladas.

## Estructura del repositorio

```
parcial-lyt/
├── punto1/          
├── punto2/         
├── punto3/          
├── punto4/           
├── punto5/           
└── README.md         
```

## Requisitos por punto

| Punto | Lenguaje | Herramientas necesarias |
|-------|----------|-------------------------|
| 1 | Python 3 | Solo Python |
| 2 | Python 3 | Solo Python |
| 3 | C | gcc, flex, bison |
| 4 | C y Python | gcc, Python 3 |
| 5 | Python 3 | Python 3, pip, antlr4-python3-runtime |

## Cómo usar este repositorio

Cada carpeta contiene su propio `README.md` con instrucciones paso a paso. A continuación un resumen rápido:

### Punto 1
```bash
cd punto1
python3 afd_movimientos.py
```

### Punto 2
```bash
cd punto2
python3 afd_identificador.py
```

### Punto 3
```bash
cd punto3
flex calculadora.l
bison -d calculadora.y
gcc lex.yy.c calculadora.tab.c -o calculadora -lm
./calculadora entrada.txt
```

### Punto 4
```bash
cd punto4
gcc fib.c -o fib
./fib
python3 fib.py
```

### Punto 5
```bash
cd punto5
python3 -m venv antlr-env
source antlr-env/bin/activate
pip install antlr4-python3-runtime
python eval_fibo.py
# Ingresar: FIBO(20)
```
