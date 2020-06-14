# Generated from /home/brayan/Documentos/UNAL/Semestre 9/Lenguajes/UNaIA/UNa-IA/Grammar/UNaIA.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .UNaIAParser import UNaIAParser
else:
    from UNaIAParser import UNaIAParser

# This class defines a complete listener for a parse tree produced by UNaIAParser.
class UNaIAListener(ParseTreeListener):

    # Enter a parse tree produced by UNaIAParser#expr.
    def enterExpr(self, ctx:UNaIAParser.ExprContext):
        pass

    # Exit a parse tree produced by UNaIAParser#expr.
    def exitExpr(self, ctx:UNaIAParser.ExprContext):
        pass


    # Enter a parse tree produced by UNaIAParser#term.
    def enterTerm(self, ctx:UNaIAParser.TermContext):
        pass

    # Exit a parse tree produced by UNaIAParser#term.
    def exitTerm(self, ctx:UNaIAParser.TermContext):
        pass


    # Enter a parse tree produced by UNaIAParser#factor.
    def enterFactor(self, ctx:UNaIAParser.FactorContext):
        pass

    # Exit a parse tree produced by UNaIAParser#factor.
    def exitFactor(self, ctx:UNaIAParser.FactorContext):
        pass



del UNaIAParser