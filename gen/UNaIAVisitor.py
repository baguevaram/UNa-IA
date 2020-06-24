# Generated from /home/brayan/Documentos/UNAL/Semestre 9/Lenguajes/UNaIA/UNa-IA/UNa-IA/Grammar/UNaIA.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .UNaIAParser import UNaIAParser
else:
    from UNaIAParser import UNaIAParser

# This class defines a complete generic visitor for a parse tree produced by UNaIAParser.

class UNaIAVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by UNaIAParser#programa.
    def visitPrograma(self, ctx:UNaIAParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#ayuda.
    def visitAyuda(self, ctx:UNaIAParser.AyudaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#DatosEjemplos.
    def visitDatosEjemplos(self, ctx:UNaIAParser.DatosEjemplosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#DatosDatos.
    def visitDatosDatos(self, ctx:UNaIAParser.DatosDatosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#AsigDatos.
    def visitAsigDatos(self, ctx:UNaIAParser.AsigDatosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#AsigModelo.
    def visitAsigModelo(self, ctx:UNaIAParser.AsigModeloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#AsigMetodo.
    def visitAsigMetodo(self, ctx:UNaIAParser.AsigMetodoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#AsigMulti.
    def visitAsigMulti(self, ctx:UNaIAParser.AsigMultiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#division.
    def visitDivision(self, ctx:UNaIAParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#modelo.
    def visitModelo(self, ctx:UNaIAParser.ModeloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#metodo.
    def visitMetodo(self, ctx:UNaIAParser.MetodoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#entrenamiento.
    def visitEntrenamiento(self, ctx:UNaIAParser.EntrenamientoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#evaluacion.
    def visitEvaluacion(self, ctx:UNaIAParser.EvaluacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#prediccion.
    def visitPrediccion(self, ctx:UNaIAParser.PrediccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#reporte.
    def visitReporte(self, ctx:UNaIAParser.ReporteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#estadisticas.
    def visitEstadisticas(self, ctx:UNaIAParser.EstadisticasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#graficas.
    def visitGraficas(self, ctx:UNaIAParser.GraficasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#exportacion.
    def visitExportacion(self, ctx:UNaIAParser.ExportacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#quantil.
    def visitQuantil(self, ctx:UNaIAParser.QuantilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#estandarizacion.
    def visitEstandarizacion(self, ctx:UNaIAParser.EstandarizacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#escaladominmax.
    def visitEscaladominmax(self, ctx:UNaIAParser.EscaladominmaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#codigo_python.
    def visitCodigo_python(self, ctx:UNaIAParser.Codigo_pythonContext):
        return self.visitChildren(ctx)



del UNaIAParser