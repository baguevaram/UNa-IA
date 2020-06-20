# Generated from /home/brayan/Documentos/UNAL/Semestre 9/Lenguajes/TESTPYTHON/Grammar/UNaIA.g4 by ANTLR 4.8
from antlr4 import *
from UNaIAParser import UNaIAParser

# Importacion de los modelos de clasificación de sklearn

from sklearn.linear_model import LogisticRegression

import csv
import os
# This class defines a complete generic visitor for a parse tree produced by UNaIAParser.

class MyVisitor(ParseTreeVisitor):

    # podemos hacer tablas aparte para los datos y los modelos, asi es mas facil identificar si existen los ids
    tabla = {}

    # TODO validar si el id existe en las asignaciones

    def visitPrograma(self, ctx: UNaIAParser.ProgramaContext):
        return self.visitChildren(ctx)

        # Visit a parse tree produced by UNaIAParser#datos.

    def visitDatos(self, ctx: UNaIAParser.DatosContext):

        return str(ctx.STRING())

        # Visit a parse tree produced by UNaIAParser#AsigDatos.

    def visitAsigDatos(self, ctx: UNaIAParser.AsigDatosContext):
        res = self.visit(ctx.datos())

        self.tabla[str(ctx.ID())] = str(res).replace('"',"")
        print("Agregué", ctx.ID(), "a la tabla y el nombre del archivo", res)
        print(self.tabla)

        return "Salí de visitAsigDatos"

        # Visit a parse tree produced by UNaIAParser#AsigModelo.

    def visitAsigModelo(self, ctx: UNaIAParser.AsigModeloContext):
        #Se visita el Nodo modelo y se agraga a la tabla de simbolos
        res = self.visit(ctx.modelo())

        if res == 'regresionLogistica':
            modelo = LogisticRegression()
        #TODO los demas modelos

        self.tabla[str(ctx.ID())] = modelo
        print("Agregué",ctx.ID(),"a la tabla y es un",modelo)
        print(self.tabla)

        return "salí de asigModelo"

        # Visit a parse tree produced by UNaIAParser#AsigMetodo.

    def visitAsigMetodo(self, ctx: UNaIAParser.AsigMetodoContext):

        res = self.visit(ctx.metodo())
        print("Agrego a la tabla",ctx.ID(),"contienen",res)
        self.tabla[str(ctx.ID())] = res
        print(self.tabla)
        return "salí de visitAsigMetodo"

        # Visit a parse tree produced by UNaIAParser#AsigMulti.

    def visitAsigMulti(self, ctx: UNaIAParser.AsigMultiContext):
        return self.visitChildren(ctx)

        # Visit a parse tree produced by UNaIAParser#division.

    def visitDivision(self, ctx: UNaIAParser.DivisionContext):

        return self.visitChildren(ctx)

        # Visit a parse tree produced by UNaIAParser#modelo.

    def visitModelo(self, ctx: UNaIAParser.ModeloContext):

        return ctx.getText()

        # Visit a parse tree produced by UNaIAParser#metodo.

    def visitMetodo(self, ctx: UNaIAParser.MetodoContext):
        return self.visitChildren(ctx)

        # Visit a parse tree produced by UNaIAParser#entrenamiento.

    def visitEntrenamiento(self, ctx: UNaIAParser.EntrenamientoContext):
        print(ctx.ID(1))
        fileName = self.tabla[str(ctx.ID(1))]
        caracteristicas=[]
        etiquetas=[]
        with open(fileName) as csvarchivo:
            entrada = csv.reader(csvarchivo)
            for reg in entrada:
                caracteristicas.append(reg[:-1])
                etiquetas.append(reg[-1])


        for i in range(len(caracteristicas)):
            for j in range(len(caracteristicas[i])):
                caracteristicas[i][j] = float(caracteristicas[i][j])

        etiquetas = [int(x) for x in etiquetas]

        print(caracteristicas)
        print(etiquetas)

        self.tabla[str(ctx.ID(0))].fit(caracteristicas,etiquetas)
        return self.visitChildren(ctx)

        # Visit a parse tree produced by UNaIAParser#evaluacion.

    def visitEvaluacion(self, ctx: UNaIAParser.EvaluacionContext):

        fileName = self.tabla[str(ctx.ID(1))]
        caracteristicas = []
        etiquetas = []
        with open(fileName) as csvarchivo:
            entrada = csv.reader(csvarchivo)
            for reg in entrada:
                caracteristicas.append(reg[:-1])
                etiquetas.append(reg[-1])

        for i in range(len(caracteristicas)):
            for j in range(len(caracteristicas[i])):
                caracteristicas[i][j] = float(caracteristicas[i][j])

        etiquetas = [int(x) for x in etiquetas]

        print(caracteristicas)
        print(etiquetas)

        res = self.tabla[str(ctx.ID(0))].score(caracteristicas, etiquetas)

        print("este es mi score")
        print(res)

        return res

        # Visit a parse tree produced by UNaIAParser#prediccion.

    def visitPrediccion(self, ctx: UNaIAParser.PrediccionContext):
        fileName = self.tabla[str(ctx.ID(1))]
        caracteristicas = []
        with open(fileName) as csvarchivo:
            entrada = csv.reader(csvarchivo)
            for reg in entrada:
                caracteristicas.append(reg[:-1])

        for i in range(len(caracteristicas)):
            for j in range(len(caracteristicas[i])):
                caracteristicas[i][j] = float(caracteristicas[i][j])

        predictions = self.tabla[str(ctx.ID(0))].predict(caracteristicas)
        print("Estas son mis predicciones")
        print(self.tabla[str(ctx.ID(0))])
        print(predictions)


        return predictions


del UNaIAParser
