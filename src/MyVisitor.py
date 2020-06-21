# Generated from /home/brayan/Documentos/UNAL/Semestre 9/Lenguajes/TESTPYTHON/Grammar/UNaIA.g4 by ANTLR 4.8
import sklearn
from antlr4 import *
from sklearn import metrics

from UNaIAParser import UNaIAParser

# Importacion de los modelos de clasificación de sklearn

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import sklearn.model_selection
import sklearn.datasets
import numpy as np
import pylab as pl
from sklearn.metrics import accuracy_score, confusion_matrix
import autosklearn.classification

import pandas as pd
import csv
import os


# This class defines a complete generic visitor for a parse tree produced by UNaIAParser.

class MyVisitor(ParseTreeVisitor):
    # podemos hacer tablas aparte para los datos y los modelos, asi es mas facil identificar si existen los ids
    tabla = {}

    # Función para visualizar un conjunto de datos en 2D
    def plot_data(self,X, y):  # Función para graficar datos (X,y)
        y_unique = np.unique(y)
        colors = pl.cm.rainbow(np.linspace(0.0, 1.0, y_unique.size))
        for this_y, color in zip(y_unique, colors):
            this_X = X[y == this_y]
            pl.scatter(this_X[:, 0], this_X[:, 1], c=np.array([color]),
                       alpha=0.5, edgecolor='k',
                       label="Class %s" % this_y)
        pl.legend(loc="best")
        pl.title("Data")

    def gen_pred_fun(self,clf):
        def pred_fun(x1, x2):
            x = np.array([[x1, x2]])
            return clf.predict(x)[0]
        return pred_fun

    # Función para visualizar de la superficie de decisión de un clasificador
    def plot_decision_region(self,X, pred_fun, num):
        min_x = np.min(X[:, 0])
        max_x = np.max(X[:, 0])
        min_y = np.min(X[:, 1])
        max_y = np.max(X[:, 1])
        min_x = min_x - (max_x - min_x) * 0.05
        max_x = max_x + (max_x - min_x) * 0.05
        min_y = min_y - (max_y - min_y) * 0.05
        max_y = max_y + (max_y - min_y) * 0.05
        x_vals = np.linspace(min_x, max_x, num)
        y_vals = np.linspace(min_y, max_y, num)
        XX, YY = np.meshgrid(x_vals, y_vals)
        grid_r, grid_c = XX.shape
        ZZ = np.zeros((grid_r, grid_c))
        for i in range(grid_r):
            for j in range(grid_c):
                ZZ[i, j] = pred_fun(XX[i, j], YY[i, j])

        pl.contourf(XX, YY, ZZ, 100, cmap=pl.cm.coolwarm, vmin=-1, vmax=2)
        pl.colorbar()
        pl.xlabel("x")
        pl.ylabel("y")

    # TODO validar si el id existe en las asignaciones

    def visitPrograma(self, ctx: UNaIAParser.ProgramaContext):
        return self.visitChildren(ctx)

        # Visit a parse tree produced by UNaIAParser#datos.

    def visitDatosEjemplos(self, ctx:UNaIAParser.DatosEjemplosContext):
        valor = str(ctx.STRING(1)).replace("\"", "")
        return (str(ctx.STRING(0)).replace('"', ""), valor)

    def visitDatosDatos(self, ctx:UNaIAParser.DatosDatosContext):
        return [str(ctx.STRING()).replace('"', "")]
        # Visit a parse tree produced by UNaIAParser#AsigDatos.

    def visitAsigDatos(self, ctx: UNaIAParser.AsigDatosContext):
        res = self.visit(ctx.datos())
        #print("Voy a revisar los datos: ", res[0])
        df = pd.read_csv(res[0])
        if len(res)>1:
            if res[1] != "None":
                etiquetas = df[res[1]]
                caracteristicas = df.drop(res[1], axis=1)
            else:
                df = pd.read_csv(res[0], header=None)
                etiquetas = df.iloc[:, -1]
                caracteristicas = df.iloc[:, :-1]

            datos_dict = {
                "etiquetas": etiquetas,
                "caracteristicas": caracteristicas
            }
            self.tabla[str(ctx.ID())] = datos_dict

        else:
            if sum(df.columns.str.contains('[A-Za-z]')) > 0:
                self.tabla[str(ctx.ID())] = df
            else:
                self.tabla[str(ctx.ID())] = pd.read_csv(res[0], header=None)

        return "Salí de visitAsigDatos"

        # Visit a parse tree produced by UNaIAParser#AsigModelo.

    def visitAsigModelo(self, ctx: UNaIAParser.AsigModeloContext):
        # Se visita el Nodo modelo y se agraga a la tabla de simbolos
        res = self.visit(ctx.modelo())

        if res == 'regresionLogistica':
            modelo = LogisticRegression()
        elif res == 'bayes':
            modelo = sklearn.naive_bayes.GaussianNB()
        elif res == 'knn':
            modelo = KNeighborsClassifier(n_neighbors=2)
        elif res == 'svm':
            modelo = sklearn.svm.NuSVC(gamma="auto")
        elif res == 'arbolDeDecision':
            modelo = DecisionTreeClassifier()
        elif res == 'bosqueAleatorio':
            modelo = RandomForestClassifier()
        elif res == 'auto':
            modelo = autosklearn.classification.AutoSklearnClassifier(time_left_for_this_task=30)

# automl.fit(X_train, y_train)
# y_hat = automl.predict(X_test)
# print("Accuracy score", accuracy_score(y_test, y_hat))

        self.tabla[str(ctx.ID())] = modelo

        return "salí de asigModelo"

        # Visit a parse tree produced by UNaIAParser#AsigMetodo.

    def visitAsigMetodo(self, ctx: UNaIAParser.AsigMetodoContext):

        res = self.visit(ctx.metodo())
        #print("Agrego a la tabla", ctx.ID(), "contienen", res)
        self.tabla[str(ctx.ID())] = res
        #print(self.tabla)
        return "salí de visitAsigMetodo"

        # Visit a parse tree produced by UNaIAParser#AsigMulti.

    def visitAsigMulti(self, ctx: UNaIAParser.AsigMultiContext):
        entrenamiento, prueba = self.visit(ctx.division())

        entrenamiento_dict = {
            "etiquetas": entrenamiento[1],
            "caracteristicas": entrenamiento[0]
        }

        pruebas_dict = {
            "etiquetas": prueba[1],
            "caracteristicas": prueba[0]
        }

        self.tabla[str(ctx.ID(0))] = entrenamiento_dict
        self.tabla[str(ctx.ID(1))] = pruebas_dict
        #print(len(entrenamiento_dict["etiquetas"]), len(pruebas_dict["etiquetas"]))
        return "Sali de AsigMulti"

        # Visit a parse tree produced by UNaIAParser#division.

    def visitDivision(self, ctx: UNaIAParser.DivisionContext):
        # Se deberia verificar que no de menos o mas de uno
        if ctx.NUMERO() == None:
            porcentaje= 70
        else:
            porcentaje = int(str(ctx.NUMERO()))

        if porcentaje > 100 or porcentaje < 0:
            raise Exception("Hubo un error semántico, Los porcentajes asignados para la"
                            " division del dataset, son superior o inferior a 100, Posición: "
                            + str(ctx.start.line) + ", " + str(ctx.getText().find(",") + ctx.start.column + 1))
        else:
            datos = self.tabla[str(ctx.ID())]
            X_train, X_test, y_train, y_test = train_test_split(
                datos["caracteristicas"], datos["etiquetas"], test_size=int(str(ctx.NUMERO()))/100)

        return (X_train, y_train), (X_test, y_test)

        # Visit a parse tree produced by UNaIAParser#modelo.

    def visitModelo(self, ctx: UNaIAParser.ModeloContext):

        return ctx.getText()

        # Visit a parse tree produced by UNaIAParser#metodo.

    def visitMetodo(self, ctx: UNaIAParser.MetodoContext):
        return self.visitChildren(ctx)

        # Visit a parse tree produced by UNaIAParser#entrenamiento.

    def visitEntrenamiento(self, ctx: UNaIAParser.EntrenamientoContext):
        #print(ctx.ID(1))
        datos = self.tabla[str(ctx.ID(1))]
        caracteristicas = datos["caracteristicas"]
        etiquetas = datos["etiquetas"]
        #print(caracteristicas)
        #print(etiquetas)
        self.tabla[str(ctx.ID(0))].fit(caracteristicas, etiquetas)
        try:
            print("CV_RESULTS: ")
            # for i in ['mean_test_score', 'mean_fit_time', 'params', 'rank_test_scores']:
            #     if type(self.tabla[str(ctx.ID(0))].cv_results_[i]) == np.ndarray:
            #         lis = self.tabla[str(ctx.ID(0))].cv_results_[i]
            #         print(i, sum(lis)/len(lis))
            #     else:
            #         print(i, self.tabla[str(ctx.ID(0))].cv_results_[i])
            print("sprint_statistics: ", self.tabla[str(ctx.ID(0))].sprint_statistics())
            # print("show_models: ", self.tabla[str(ctx.ID(0))].show_models())
        except Exception:
            pass
        return "Terminado el Entrenamiento"

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
        predictions = self.tabla[str(ctx.ID(0))].predict(datos)
        print("Encontre ", sum(predictions), "valores de 1 y ", 100-sum(predictions), "valores de 0")
        #print(self.tabla[str(ctx.ID(0))])
        pruebas_dict = {
            "etiquetas": predictions,
            "caracteristicas": datos
        }
        #print(datos.head())
        return pruebas_dict

    # Visit a parse tree produced by UNaIAParser#reporte.
    def visitReporte(self, ctx: UNaIAParser.ReporteContext):
        rows = int(str(ctx.NUMERO(0))) if ctx.NUMERO(0) != None else None
        cols = int(str(ctx.NUMERO(1))) if ctx.NUMERO(1) != None else None

        datos = self.tabla[str(ctx.ID())]
        with pd.option_context('display.max_rows', rows, 'display.max_columns', cols):
            print("Las Caracteristicas del DataFrame son las siguientes: ")
            print(datos["caracteristicas"])
            print("\nSu Análisis Descriptivo es el siguiente: ")
            print(datos["caracteristicas"].describe(include='all'))

            print("\nLas Etiquetas del DataFrame son las siguientes: ")
            print(datos["etiquetas"])
            print("\nSu Análisis Descriptivo es el siguiente: ")
            print(datos["etiquetas"].describe(include='all'))



        return self.visitChildren(ctx)

    # Visit a parse tree produced by UNaIAParser#estadisticas.
    def visitEstadisticas(self, ctx: UNaIAParser.EstadisticasContext):
        datos = self.tabla[str(ctx.ID(1))]
        # print(datos)
        caracteristicas = datos["caracteristicas"]
        etiquetas = datos["etiquetas"]

        predictions = self.tabla[str(ctx.ID(0))].predict(caracteristicas)

        cnf_matrix = confusion_matrix(etiquetas, predictions)

        print("\nMatriz de confusion")
        print(cnf_matrix)

        print('\nPrecision: {}'.format(metrics.precision_score(etiquetas, predictions, average='micro')))
        print('Recall: {}'.format(metrics.recall_score(etiquetas, predictions, average='micro')))
        print('Puntaje F_1: {}'.format(metrics.f1_score(etiquetas, predictions, average='micro')))

        return self.visitChildren(ctx)

    # Visit a parse tree produced by UNaIAParser#graficas.
    def visitGraficas(self, ctx: UNaIAParser.GraficasContext):
        datos = self.tabla[str(ctx.ID(1))]
        caracteristicas = datos["caracteristicas"]
        etiquetas = datos["etiquetas"]
        num = 100
        if str(self.tabla[str(ctx.ID(0))])[0:4] == "Auto":
            print("Usted Eligio un Modelo automático, su gráfica se puede demorar, espere por favor: ")
            num = 10
        self.plot_decision_region(caracteristicas.values, self.gen_pred_fun(self.tabla[str(ctx.ID(0))]), num)
        self.plot_data(caracteristicas.values, etiquetas.values)
        pl.show()
        return self.visitChildren(ctx)

del UNaIAParser
