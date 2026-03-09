import sys
from antlr4 import *
from FibonacciLexer import FibonacciLexer
from FibonacciParser import FibonacciParser
from FibonacciVisitor import FibonacciVisitor

class EvalFibonacciVisitor(FibonacciVisitor):
    """
    Visitor personalizado que recorre el árbol sintáctico
    y calcula la serie de Fibonacci.
    """
    
    def visitProg(self, ctx):
        """
        Método para la regla 'prog': visita el comando y retorna su resultado.
        """
        return self.visit(ctx.comando())  
    
    def visitComando(self, ctx):
        """
        Se llama cuando se encuentra la regla 'comando'.
        Extrae el número entero y calcula la serie.
        """
        n_text = ctx.INT().getText()
        n = int(n_text)
        
        serie = []
        a, b = 0, 1
        while a <= n:
            serie.append(str(a))
            a, b = b, a + b
        
        return ", ".join(serie) 

def main():
    print("Ingrese el comando (ej: FIBO(20)):")
    linea = sys.stdin.readline().strip()
    
    input_stream = InputStream(linea)
    lexer = FibonacciLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = FibonacciParser(token_stream)
    
    tree = parser.prog()
    
    visitor = EvalFibonacciVisitor()
    resultado = visitor.visit(tree)   
    
    print(f"\nResultado: {resultado}")

if __name__ == "__main__":
    main()
