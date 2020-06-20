# Generated from /home/brayan/Documentos/UNAL/Semestre 9/Lenguajes/TESTPYTHON/Grammar/UNaIA.g4 by ANTLR 4.8
from antlr4 import *
from UNaIAParser import UNaIAParser

# Importacion de los modelos de clasificación de sklearn

from sklearn.linear_model import LogisticRegression
import pandas as pd
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
        valor = str(ctx.STRING(1)).replace("\"", "")
        return (str(ctx.STRING(0)).replace('"', ""), valor)

        # Visit a parse tree produced by UNaIAParser#AsigDatos.

    def visitAsigDatos(self, ctx: UNaIAParser.AsigDatosContext):
        res = self.visit(ctx.datos())
        df = pd.read_csv(res[0])
        if res[1] == "None":
            df = pd.read_csv(res[0], header=None)
            etiquetas = df[res[1]]
            caracteristicas = df.drop(res[1], axis=1)
        else:
            etiquetas = df.iloc[:, -1]
            caracteristicas = df.iloc[:, :-1]

        datos_dict = {
            "df": df,
            "etiquetas": etiquetas,
            "caracteristicas": caracteristicas
        }
        self.tabla[str(ctx.ID())] = datos_dict

        #print("Agregué", ctx.ID(), "a la tabla y el nombre del archivo", res)
        #print(self.tabla)
        return "Salí de visitAsigDatos"

        # Visit a parse tree produced by UNaIAParser#AsigModelo.

    def visitAsigModelo(self, ctx: UNaIAParser.AsigModeloContext):
        # Se visita el Nodo modelo y se agraga a la tabla de simbolos
        res = self.visit(ctx.modelo())

        if res == 'regresionLogistica':
            modelo = LogisticRegression()
        # TODO los demas modelos

        self.tabla[str(ctx.ID())] = modelo
        #print("Agregué", ctx.ID(), "a la tabla y es un", modelo)
        #print(self.tabla)

        return "salí de asigModelo"

        # Visit a parse tree produced by UNaIAParser#AsigMetodo.

    def visitAsigMetodo(self, ctx: UNaIAParser.AsigMetodoContext):

        res = self.visit(ctx.metodo())
        print("Agrego a la tabla", ctx.ID(), "contienen", res)
        self.tabla[str(ctx.ID())] = res
        print(self.tabla)
        return "salí de visitAsigMetodo"

        # Visit a parse tree produced by UNaIAParser#AsigMulti.

    def visitAsigMulti(self, ctx: UNaIAParser.AsigMultiContext):
        return self.visitChildren(ctx)

        # Visit a parse tree produced by UNaIAParser#division.

    def visitDivision(self, ctx: UNaIAParser.DivisionContext):
        # Se deberia verificar que no de menos o mas de uno

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
        datos = self.tabla[str(ctx.ID(1))]
        caracteristicas = datos["caracteristicas"]
        etiquetas = datos["etiquetas"]
        #print(caracteristicas)
        #print(etiquetas)
        self.tabla[str(ctx.ID(0))].fit(caracteristicas, etiquetas)
        return self.visitChildren(ctx)

        # Visit a parse tree produced by UNaIAParser#evaluacion.

    def visitEvaluacion(self, ctx: UNaIAParser.EvaluacionContext):

        datos = self.tabla[str(ctx.ID(1))]
        caracteristicas = datos["caracteristicas"]
        etiquetas = datos["etiquetas"]

        #print(caracteristicas)
        #print(etiquetas)

        res = self.tabla[str(ctx.ID(0))].score(caracteristicas, etiquetas)

        print("este es mi score")
        print(res)

        return res

        # Visit a parse tree produced by UNaIAParser#prediccion.

    def visitPrediccion(self, ctx: UNaIAParser.PrediccionContext):
        datos = self.tabla[str(ctx.ID(1))]
        caracteristicas = datos["caracteristicas"]

        predictions = self.tabla[str(ctx.ID(0))].predict(caracteristicas)
        #print("Estas son mis predicciones")
        #print(self.tabla[str(ctx.ID(0))])
        #print(predictions)

        return predictions


del UNaIAParser
