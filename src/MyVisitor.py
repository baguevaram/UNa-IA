# Generated from /home/brayan/Documentos/UNAL/Semestre 9/Lenguajes/TESTPYTHON/Grammar/UNaIA.g4 by ANTLR 4.8
from antlr4 import *
from UNaIAParser import UNaIAParser


# This class defines a complete generic visitor for a parse tree produced by UNaIAParser.

class MyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by UNaIAParser#UNaIA.
    def visitExpr(self, ctx: UNaIAParser.ExprContext):
        print("Soy una UNaIAesion")
        print("Tengo ", len(ctx.MAS()), " sumas")
        print("Tengo ", len(ctx.MENOS()), " restas")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by UNaIAParser#term.
    def visitTerm(self, ctx: UNaIAParser.TermContext):
        print("Soy un termino")
        print("Tengo ", len(ctx.MULT()), " multiplicaciones")
        print("Tengo ", len(ctx.DIV()), " divisiones")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by UNaIAParser#factor.
    def visitFactor(self, ctx: UNaIAParser.FactorContext):
        print("Soy un factor y mi lexema es: ", ctx.ENTERO())
        return self.visitChildren(ctx)


del UNaIAParser
