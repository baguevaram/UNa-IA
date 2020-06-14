# Generated from /home/brayan/Documentos/UNAL/Semestre 9/Lenguajes/UNaIA/UNa-IA/Grammar/UNaIA.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .UNaIAParser import UNaIAParser
else:
    from UNaIAParser import UNaIAParser

# This class defines a complete generic visitor for a parse tree produced by UNaIAParser.

class UNaIAVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by UNaIAParser#expr.
    def visitExpr(self, ctx:UNaIAParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#term.
    def visitTerm(self, ctx:UNaIAParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#factor.
    def visitFactor(self, ctx:UNaIAParser.FactorContext):
        return self.visitChildren(ctx)



del UNaIAParser