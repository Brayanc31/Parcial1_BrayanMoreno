import time

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def main():
    n = 45
    inicio = time.perf_counter()
    resultado = fib(n)
    fin = time.perf_counter()
    tiempo = fin - inicio

    print(f"Fibonacci({n}) = {resultado}")
    print(f"Tiempo en Python: {tiempo:.6f} segundos")

if __name__ == "__main__":
    main()
