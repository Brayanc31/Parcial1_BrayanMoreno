# Generated from Fibonacci.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FibonacciParser import FibonacciParser
else:
    from FibonacciParser import FibonacciParser

# This class defines a complete listener for a parse tree produced by FibonacciParser.
class FibonacciListener(ParseTreeListener):

    # Enter a parse tree produced by FibonacciParser#prog.
    def enterProg(self, ctx:FibonacciParser.ProgContext):
        pass

    # Exit a parse tree produced by FibonacciParser#prog.
    def exitProg(self, ctx:FibonacciParser.ProgContext):
        pass


    # Enter a parse tree produced by FibonacciParser#comando.
    def enterComando(self, ctx:FibonacciParser.ComandoContext):
        pass

    # Exit a parse tree produced by FibonacciParser#comando.
    def exitComando(self, ctx:FibonacciParser.ComandoContext):
        pass



del FibonacciParser