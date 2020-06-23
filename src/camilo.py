from antlr4 import *
from UNaIAParser import UNaIAParser

# Importacion de los modelos de clasificación de sklearn
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve
from sklearn.metrics import accuracy_score, confusion_matrix
import sklearn.model_selection
import sklearn.datasets
from sklearn import metrics
from sklearn import preprocessing
from collections import Counter
import numpy as np
import pylab as pl
import autosklearn.classification
import matplotlib.pyplot as plt
import pandas as pd
import os, sys
import PIL

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

# This class defines a complete generic visitor for a parse tree produced by UNaIAParser.

# Cleaning if exists output python code
output_path = "../output/UNaIAModel.py"
if os.path.exists(output_path):
    os.remove(output_path)

imports = "import sklearn\n" \
          "from sklearn.linear_model import LogisticRegression\n" \
          "from sklearn.neighbors import KNeighborsClassifier\n" \
          "from sklearn.tree import DecisionTreeClassifier\n" \
          "from sklearn.ensemble import RandomForestClassifier\n" \
          "from sklearn.model_selection import train_test_split\n" \
          "from sklearn.model_selection import learning_curve\n" \
          "from sklearn.metrics import accuracy_score, confusion_matrix\n" \
          "import sklearn.model_selection\n" \
          "import sklearn.datasets\n" \
          "from sklearn import metrics\n" \
          "from sklearn import preprocessing\n" \
          "from collections import Counter\n" \
          "import numpy as np\n" \
          "import pylab as pl\n" \
          "import autosklearn.classification\n" \
          "import matplotlib.pyplot as plt\n" \
          "import pandas as pd\n" \
          "import os, sys\n" \
          "import PIL\n"

with open(output_path, "a") as file:
    file.write(imports)

class MyVisitor(ParseTreeVisitor):

    ##########################################################################################################################
    #                                       GLOBAL DEFINITIONS                                                               #
    ##########################################################################################################################
    # podemos hacer tablas aparte para los datos y los modelos, asi es mas facil identificar si existen los ids
    tabla = {}
    ##########################################################################################################################
    #                                       ERROR HANDLING FUNCTIONS                                                         #
    ##########################################################################################################################
    # functions needed to error detection
    def get_error(self, error):
        reverse = error[::-1]
        result = ''
        for i in range(2, len(reverse)):
            if reverse[i] != "'" and reverse[i] != ".":
                result += reverse[i]
            else:
                break
        return re.findall('[A-Z][^A-Z]*', result[::-1])

    def get_error_translation(self, error_list):
        error_str = ''
        for st in error_list:
            error_str += st + ' '
        translator = Translator()
        print(translator.detect('Soy una salsa bechamel'))
        translation = translator.translate(error_str, src='en', dest='es')
        return translation.text

    def print_error(self, error):
        return self.get_error_translation(self.get_error(str(error)))

    ##########################################################################################################################
    #                                       INTERNAL FUNCTIONS                                                               #
    ##########################################################################################################################

    def plot_learning_curve(self, estimator, title, X, y, axes=None, ylim=None, cv=None,
                            n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
        if axes is None:
            _, axes = plt.subplots(1, 1)

        axes.set_title(title)
        if ylim is not None:
            axes.set_ylim(*ylim)
        axes.set_xlabel("Ejemplos de Entrenamiento")
        axes.set_ylabel("Puntaje")

        train_sizes, train_scores, test_scores, fit_times, _ = \
            learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs,
                           train_sizes=train_sizes,
                           return_times=True)
        train_scores_mean = np.mean(train_scores, axis=1)
        train_scores_std = np.std(train_scores, axis=1)
        test_scores_mean = np.mean(test_scores, axis=1)
        test_scores_std = np.std(test_scores, axis=1)

        # Plot learning curve
        axes.grid()
        axes.fill_between(train_sizes, train_scores_mean - train_scores_std,
                             train_scores_mean + train_scores_std, alpha=0.1,
                             color="r")
        axes.fill_between(train_sizes, test_scores_mean - test_scores_std,
                             test_scores_mean + test_scores_std, alpha=0.1,
                             color="g")
        axes.plot(train_sizes, train_scores_mean, 'o-', color="r",
                     label="Puntaje de entrenamiento")
        axes.plot(train_sizes, test_scores_mean, 'o-', color="g",
                     label="Puntaje de validación cruzada")
        axes.legend(loc="best")

    def_plot_learning_curve = "    \ndef plot_learning_curve(self, estimator, title, X, y, axes=None, ylim=None, cv=None,\n" \
                              "                             n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):\n" \
                              "        if axes is None:\n" \
                              "            _, axes = plt.subplots(1, 1)\n" \
                              "        axes.set_title(title)\n" \
                              "        if ylim is not None:\n" \
                              "            axes.set_ylim(*ylim)\n" \
                              "        axes.set_xlabel(\"Ejemplos de Entrenamiento\")\n" \
                              "        axes.set_ylabel(\"Puntaje\")\n" \
                              "        train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs,\n" \
                              "                           train_sizes=train_sizes,\n" \
                              "                           return_times=True)\n" \
                              "        train_scores_mean = np.mean(train_scores, axis=1)\n" \
                              "        train_scores_std = np.std(train_scores, axis=1)\n" \
                              "        test_scores_mean = np.mean(test_scores, axis=1)\n" \
                              "        test_scores_std = np.std(test_scores, axis=1)\n" \
                              "        # Plot learning curve\n" \
                              "        axes.grid()\n" \
                              "        axes.fill_between(train_sizes, train_scores_mean - train_scores_std,\n" \
                              "                          train_scores_mean + train_scores_std, alpha=0.1,\n" \
                              "                          color=\"r\")\n" \
                              "        axes.fill_between(train_sizes, test_scores_mean - test_scores_std,\n" \
                              "                          test_scores_mean + test_scores_std, alpha=0.1,\n" \
                              "                          color=\"g\")\n" \
                              "        axes.plot(train_sizes, train_scores_mean, 'o-', color=\"r\",\n" \
                              "                  label=\"Puntaje de entrenamiento\")\n" \
                              "        axes.plot(train_sizes, test_scores_mean, 'o-', color=\"g\",\n" \
                              "                   label=\"Puntaje de validación cruzada\")\n" \
                              "        axes.legend(loc=\"best\")\n"

    with open (output_path,"a") as file:
        file.write(def_plot_learning_curve)

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

    def_plot_data = "\n# Función para visualizar un conjunto de datos en 2D\n" \
                    "def plot_data(self, X, y):  # Función para graficar datos (X,y)\n" \
                    "   y_unique = np.unique(y)\n" \
                    "   colors = pl.cm.rainbow(np.linspace(0.0, 1.0, y_unique.size))\n" \
                    "   for this_y, color in zip(y_unique, colors):\n" \
                    "       this_X = X[y == this_y]\n" \
                    "       pl.scatter(this_X[:, 0], this_X[:, 1], c=np.array([color]),\n" \
                    "       alpha=0.5, edgecolor='k',\n" \
                    "       label=\"Class %s\" % this_y)\n" \
                    "       pl.legend(loc=\"best\")\n" \
                    "       pl.title(\"Data\")\n"

    with open (output_path, "a") as file:
        file.write(def_plot_data)

    def gen_pred_fun(self,clf):
        def pred_fun(x1, x2):
            x = np.array([[x1, x2]])
            return clf.predict(x)[0]
        return pred_fun

    def_gen_pred_fun = "\ndef gen_pred_fun(self, clf):\n" \
                       "    def pred_fun(x1, x2):\n" \
                       "        x = np.array([[x1, x2]])\n" \
                       "        return clf.predict(x)[0]\n" \
                       "    return pred_fun\n"

    with open (output_path,"a") as file:
        file.write(def_gen_pred_fun)

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
        blockPrint()
        for i in range(grid_r):
            for j in range(grid_c):

                ZZ[i, j] = pred_fun(XX[i, j], YY[i, j])
        enablePrint()
        pl.contourf(XX, YY, ZZ, 100, cmap=pl.cm.coolwarm, vmin=-1, vmax=2)
        pl.colorbar()
        pl.xlabel("x")
        pl.ylabel("y")

    def_plot_decision_region = "\ndef plot_decision_region(self, X, pred_fun):\n" \
                               "    min_x = np.min(X[:, 0])\n" \
                               "    max_x = np.max(X[:, 0])\n" \
                               "    min_y = np.min(X[:, 1])\n" \
                               "    max_y = np.max(X[:, 1])\n" \
                               "    min_x = min_x - (max_x - min_x) * 0.05\n" \
                               "    max_x = max_x + (max_x - min_x) * 0.05\n" \
                               "    min_y = min_y - (max_y - min_y) * 0.05\n" \
                               "    max_y = max_y + (max_y - min_y) * 0.05\n" \
                               "    x_vals = np.linspace(min_x, max_x, 100)\n" \
                               "    y_vals = np.linspace(min_y, max_y, 100)\n" \
                               "    XX, YY = np.meshgrid(x_vals, y_vals)\n" \
                               "    grid_r, grid_c = XX.shape\n" \
                               "    ZZ = np.zeros((grid_r, grid_c))\n" \
                               "    for i in range(grid_r):\n" \
                               "        for j in range(grid_c):\n" \
                               "            ZZ[i, j] = pred_fun(XX[i, j], YY[i, j])\n" \
                               "    pl.contourf(XX, YY, ZZ, 100, cmap=pl.cm.coolwarm, vmin=-1, vmax=2)\n" \
                               "    pl.colorbar()\n" \
                               "    pl.xlabel(\"x\")\n" \
                               "    pl.ylabel(\"y\")\n\n\n"

    with open (output_path,"a") as file:
        file.write(def_plot_decision_region)

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
        instruction = ''
        res = self.visit(ctx.datos())
        #print("Voy a revisar los datos: ", res[0])
        #print("ctx de visitAsigDatos tiene ",ctx.getText())
        ID = str(ctx.ID())
        df = pd.read_csv(res[0])
        instruction+= ID + ' = pd.read_csv(\"' + str(res[0]) + '\")\n'
        if len(res)>1:
            if res[1] != "None":
                etiquetas = df[res[1]]
                caracteristicas = df.drop(res[1], axis=1)
                instruction +='X = '+ID+'.drop(\"'+res[1]+'\", axis=1)\n'
                instruction +='y = ' + ID +'[\"'+res[1]+'\"]\n'
            else:
                df = pd.read_csv(res[0], header=None)
                etiquetas = df.iloc[:, -1]
                caracteristicas = df.iloc[:, :-1]
                instruction += ID+'=pd.read_csv(\"'+res[0]+ '\", header=None)\n'
                instruction += 'X = ' + ID + '.iloc[:, :-1]\n'
                instruction += 'y = ' + ID + '.iloc[:, :-1]\n'
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
        with open (output_path, "a") as file:
            file.write(instruction)
        return "Salí de visitAsigDatos"

        # Visit a parse tree produced by UNaIAParser#AsigModelo.

    def visitAsigModelo(self, ctx: UNaIAParser.AsigModeloContext):
        # Se visita el Nodo modelo y se agraga a la tabla de simbolos
        #print("visitAsigModelo tiene ",ctx.getText())
        instruction = ''
        ID = ctx.ID()
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

        self.tabla[str(ctx.ID())] = modelo

        instruction = str(ID)+' = '+str(modelo)+'\n'
        with open (output_path, "a") as file:
            file.write(instruction)

        return "salí de asigModelo"

        # Visit a parse tree produced by UNaIAParser#AsigMetodo.

    def visitAsigMetodo(self, ctx: UNaIAParser.AsigMetodoContext):
        print("visitAsigMetodo tiene ",ctx.getText())
        print("WTF")
        with open (output_path,"a") as file:
            file.write("ESTOY ENTRANDO EN UNA ASIGNACION DE UN MÉTODO")
        res = self.visit(ctx.metodo())
        #print("Agrego a la tabla", ctx.ID(), "contienen", res)
        self.tabla[str(ctx.ID())] = res
        #print(self.tabla)
        return "salí de visitAsigMetodo"

        # Visit a parse tree produced by UNaIAParser#AsigMulti.

    def visitAsigMulti(self, ctx: UNaIAParser.AsigMultiContext):
        print("visitAsigMulti tiene ", ctx.getText())

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
        print("visitDivision tiene ", ctx.getText())
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

        instruction = 'X_train, X_test, y_train, y_test =  train_test_split(' \
                      'X, y, ' \
                      'test_size=int('+str(ctx.NUMERO())+'))\n'
        with open (output_path,"a") as file:
            file.write(instruction)
        return (X_train, y_train), (X_test, y_test)

        # Visit a parse tree produced by UNaIAParser#modelo.

    def visitModelo(self, ctx: UNaIAParser.ModeloContext):
        print("visitModelo tiene ", ctx.getText())
        return ctx.getText()

        # Visit a parse tree produced by UNaIAParser#metodo.

    def visitMetodo(self, ctx: UNaIAParser.MetodoContext):
        print("visitMetodo tiene ", ctx.getText())
        return self.visitChildren(ctx)

        # Visit a parse tree produced by UNaIAParser#entrenamiento.

    def visitEntrenamiento(self, ctx: UNaIAParser.EntrenamientoContext):
        print("visitEntrenamiento tiene ", ctx.getText())
        datos = self.tabla[str(ctx.ID(1))]
        caracteristicas = datos["caracteristicas"]
        etiquetas = datos["etiquetas"]
        instruction =str(ctx.ID(0)) +".fit(X_train,y_train)\n"
        with open (output_path, "a") as file :
            file.write(instruction)
        #blockPrint()
        self.tabla[str(ctx.ID(0))].fit(caracteristicas, etiquetas)
        #enablePrint()
        try:
            print("\n\n#####################################################")
            print("Resultados de la Validación Cruzada para el Modelo", str(ctx.ID(0)), ":\n")
            modl_name = Counter()
            for i in ['mean_test_score', 'mean_fit_time', 'params']:
                if type(self.tabla[str(ctx.ID(0))].cv_results_[i]) == np.ndarray:
                    lis = self.tabla[str(ctx.ID(0))].cv_results_[i]
                    print(i, sum(lis)/len(lis))
                else:
                    print("\nConteo de modelos entrenados y sus tipos: ")
                    modl = self.tabla[str(ctx.ID(0))].cv_results_[i]
                    for j in modl:
                        # print(i)
                        modl_name[j["classifier:__choice__"]] += 1
            for i in modl_name:
                print("Numero de", i, " entrenados:", modl_name[i])
            print("#####################################################\n\n")
            print("#####################################################")
            print("Resultados de Auto Sklearn para el Modelo", str(ctx.ID(0)), ":\n")
            lis = [i.replace("\n", "") for i in self.tabla[str(ctx.ID(0))].sprint_statistics().split("  ")]
            print(lis[2])
            print(lis[3])
            print(lis[4])
            print("#####################################################\n\n")
        except Exception:
            pass
        return "Terminado el Entrenamiento"

        # Visit a parse tree produced by UNaIAParser#evaluacion.

    def visitEvaluacion(self, ctx: UNaIAParser.EvaluacionContext):
        print("visitEntvaluacion tiene ", ctx.getText())
        datos = self.tabla[str(ctx.ID(1))]
        caracteristicas = datos["caracteristicas"]
        etiquetas = datos["etiquetas"]

        #print(caracteristicas)
        #print(etiquetas)

        res = self.tabla[str(ctx.ID(0))].score(caracteristicas, etiquetas)
        print("#####################################################")
        print("Desempeño del modelo", str(ctx.ID(0)), ":", res)
        print("#####################################################\n\n")
        instruction = str(ctx.ID(0))+".score(X, y)\n"
        with open (output_path, "a") as file:
            file.write(instruction)
        return res

        # Visit a parse tree produced by UNaIAParser#prediccion.

    def visitPrediccion(self, ctx: UNaIAParser.PrediccionContext):
        print("visitPredicciontiene ", ctx.getText())
        datos = self.tabla[str(ctx.ID(1))]
        predictions = self.tabla[str(ctx.ID(0))].predict(datos)
        #print(self.tabla[str(ctx.ID(0))])
        pruebas_dict = {
            "etiquetas": predictions,
            "caracteristicas": datos
        }
        #print(datos.head())
        instruction = str(ctx.ID(0))+".predict("+str(ctx.ID(1))+")\n"
        with open (output_path, "a") as file:
            file.write(instruction)
        return pruebas_dict

    # Visit a parse tree produced by UNaIAParser#reporte.
    def visitReporte(self, ctx: UNaIAParser.ReporteContext):
        rows = int(str(ctx.NUMERO(0))) if ctx.NUMERO(0) != None else None
        cols = int(str(ctx.NUMERO(1))) if ctx.NUMERO(1) != None else None

        datos = self.tabla[str(ctx.ID())]
        with pd.option_context('display.max_rows', rows, 'display.max_columns', cols):
            print("#####################################################")
            print("Las Caracteristicas del DataFrame son las siguientes: ")
            print(datos["caracteristicas"])
            print("\nSu Análisis Descriptivo es el siguiente: ")
            print(datos["caracteristicas"].describe(include='all'))
            print("#####################################################\n\n")

            print("#####################################################")
            print("\nLas Etiquetas del DataFrame son las siguientes: ")
            print(datos["etiquetas"])
            print("\nSu Análisis Descriptivo es el siguiente: ")
            print(datos["etiquetas"].describe(include='all'))
            print("#####################################################\n\n")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by UNaIAParser#estadisticas.
    def visitEstadisticas(self, ctx: UNaIAParser.EstadisticasContext):
        datos = self.tabla[str(ctx.ID(1))]
        # print(datos)
        caracteristicas = datos["caracteristicas"]
        etiquetas = datos["etiquetas"]

        predictions = self.tabla[str(ctx.ID(0))].predict(caracteristicas)

        cnf_matrix = confusion_matrix(etiquetas, predictions)

        print("#####################################################")
        print("Matriz de confusion del modelo", str(ctx.ID(0)), ":\n")
        print(cnf_matrix)
        print("#####################################################\n\n")

        print("#####################################################")
        print("Resultados del modelo", str(ctx.ID(0)), ":\n")
        print('Precision: {}'.format(metrics.precision_score(etiquetas, predictions, average='micro')))
        print('Recall: {}'.format(metrics.recall_score(etiquetas, predictions, average='micro')))
        print('Puntaje F_1: {}'.format(metrics.f1_score(etiquetas, predictions, average='micro')))
        print("#####################################################\n\n")


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

        ruta = ""
        nombre = "RegionDeDecision" + str(ctx.ID(0)) + '.jpg'

        if ctx.EN() != None:
            ruta += str(ctx.STRING(0)).replace('"', "") + '/'
            if ctx.COMO() != None:
                nombre = str(ctx.STRING(1)).replace('"', "") + ".jpg"
        elif ctx.COMO() != None:
            nombre = str(ctx.STRING(0)).replace('"', "") + ".jpg"

        ruta += nombre
        pl.title("Region de Decision de " + str(ctx.ID(0)))
        pl.savefig(ruta, bbox_inches='tight')
        pl.show()
        if str(self.tabla[str(ctx.ID(0))])[0:4] != "Auto":
            self.plot_learning_curve(self.tabla[str(ctx.ID(0))], "Curva de aprendizaje de " + str(ctx.ID(0)),
                                     caracteristicas, etiquetas, axes=None, ylim=None, cv=None)

            ruta = ""
            nombre = "CurvaDeAprendizaje" + str(ctx.ID(0)) + '.jpg'

            if ctx.EN() != None:
                ruta += str(ctx.STRING(0)).replace('"', "") + '/'
                if ctx.Y() != None:
                    nombre = str(ctx.STRING(2)).replace('"', "") + ".jpg"
            elif ctx.Y() != None:
                nombre = str(ctx.STRING(1)).replace('"', "") + ".jpg"

            ruta += nombre

            plt.savefig(ruta, bbox_inches='tight')
            plt.show()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by UNaIAParser#exportacion.
    def visitExportacion(self, ctx: UNaIAParser.ExportacionContext):

        datos = self.tabla[str(ctx.ID())]

        if type(datos) != pd.core.frame.DataFrame:
            df = datos["caracteristicas"]
            df["Etiquetas"] = datos["etiquetas"]
        else:
            df = datos

        ruta = ""
        nombre = str(ctx.ID()) + '.csv'

        if ctx.EN() != None:
            ruta += str(ctx.STRING(0)).replace('"',"") + '/'
            if ctx.COMO() != None:
                nombre = str(ctx.STRING(1)).replace('"', "") + ".csv"
        elif ctx.COMO() != None :
            nombre = str(ctx.STRING(0)).replace('"', "") + ".csv"

        ruta += nombre

        df.to_csv(ruta, index=False)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by UNaIAParser#normalizacion.
    def visitQuantil(self, ctx:UNaIAParser.QuantilContext):
        datos = self.tabla[str(ctx.ID())]
        datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")] = datos["caracteristicas"][
            str(ctx.STRING()).replace("\"", "")].values.astype(float)
        q_scale = preprocessing.QuantileTransformer()
        col_scaled = q_scale.fit_transform(datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")].values.reshape(-1, 1))
        datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")] = col_scaled
        self.tabla[str(ctx.ID())] = datos

        return "Ha sido Normalizado Correctamente"

    # Visit a parse tree produced by UNaIAParser#estandarizacion.
    def visitEstandarizacion(self, ctx:UNaIAParser.EstandarizacionContext):
        datos = self.tabla[str(ctx.ID())]
        datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")] = datos["caracteristicas"][
            str(ctx.STRING()).replace("\"", "")].values.astype(float)
        std_scaler = preprocessing.StandardScaler()
        col_scaled = std_scaler.fit_transform(
            datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")].values.reshape(-1, 1))
        datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")] = col_scaled
        self.tabla[str(ctx.ID())] = datos
        return "Ha sido Estandarizado correctamente"


    # Visit a parse tree produced by UNaIAParser#escaladominmax.
    def visitEscaladominmax(self, ctx:UNaIAParser.EscaladominmaxContext):
        datos = self.tabla[str(ctx.ID())]
        datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")] = datos["caracteristicas"][
            str(ctx.STRING()).replace("\"", "")].values.astype(float)
        min_max_scaler = preprocessing.MinMaxScaler()
        col_scaled = min_max_scaler.fit_transform(
            datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")].values.reshape(-1, 1))
        datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")] = col_scaled
        self.tabla[str(ctx.ID())] = datos
        return "Ha sido Escalado Correctamente"
del UNaIAParser
