# Generated from /home/brayan/Documentos/UNAL/Semestre 9/Lenguajes/TESTPYTHON/Grammar/UNaIA.g4 by ANTLR 4.8
from collections import Counter
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
from sklearn.naive_bayes import GaussianNB

import numpy as np
import pylab as pl
import autosklearn.classification
import matplotlib.pyplot as plt
import pandas as pd
import os, sys
import PIL
from googletrans import Translator
import re

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')


# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


# This class defines a complete generic visitor for a parse tree produced by UNaIAParser.

class MyVisitor(ParseTreeVisitor):
    # Plantilla
    ########################################################################################

    plantilla = "import sklearn\n" \
                "from sklearn.linear_model import LogisticRegression\n" \
                "from sklearn.neighbors import KNeighborsClassifier\n" \
                "from sklearn.tree import DecisionTreeClassifier\n" \
                "from sklearn.ensemble import RandomForestClassifier\n" \
                "from sklearn.model_selection import train_test_split\n" \
                "from sklearn.model_selection import learning_curve\n" \
                "from sklearn.naive_bayes import GaussianNB\n" \
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
                "import PIL\n\n" \
                "\ndef plot_learning_curve(estimator, title, X, y, axes=None, ylim=None, cv=None,\n" \
                "                         n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):\n" \
                "    if axes is None:\n" \
                "        _, axes = plt.subplots(1, 1)\n" \
                "    axes.set_title(title)\n" \
                "    if ylim is not None:\n" \
                "        axes.set_ylim(*ylim)\n" \
                "    axes.set_xlabel(\"Ejemplos de Entrenamiento\")\n" \
                "    axes.set_ylabel(\"Puntaje\")\n" \
                "    train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs,\n" \
                "                       train_sizes=train_sizes,\n" \
                "                       return_times=True, shuffle=True)\n" \
                "    train_scores_mean = np.mean(train_scores, axis=1)\n" \
                "    train_scores_std = np.std(train_scores, axis=1)\n" \
                "    test_scores_mean = np.mean(test_scores, axis=1)\n" \
                "    test_scores_std = np.std(test_scores, axis=1)\n" \
                "    # Plot learning curve\n" \
                "    axes.grid()\n" \
                "    axes.fill_between(train_sizes, train_scores_mean - train_scores_std,\n" \
                "                      train_scores_mean + train_scores_std, alpha=0.1,\n" \
                "                      color=\"r\")\n" \
                "    axes.fill_between(train_sizes, test_scores_mean - test_scores_std,\n" \
                "                      test_scores_mean + test_scores_std, alpha=0.1,\n" \
                "                      color=\"g\")\n" \
                "    axes.plot(train_sizes, train_scores_mean, 'o-', color=\"r\",\n" \
                "              label=\"Puntaje de entrenamiento\")\n" \
                "    axes.plot(train_sizes, test_scores_mean, 'o-', color=\"g\",\n" \
                "               label=\"Puntaje de validación cruzada\")\n" \
                "    axes.legend(loc=\"best\")\n" \
                "\n# Función para visualizar un conjunto de datos en 2D\n" \
                "def plot_data(X, y):  # Función para graficar datos (X,y)\n" \
                "   y_unique = np.unique(y)\n" \
                "   colors = pl.cm.rainbow(np.linspace(0.0, 1.0, y_unique.size))\n" \
                "   for this_y, color in zip(y_unique, colors):\n" \
                "       this_X = X[y == this_y]\n" \
                "       pl.scatter(this_X[:, 0], this_X[:, 1], c=np.array([color]),\n" \
                "       alpha=0.5, edgecolor='k',\n" \
                "       label=\"Class %s\" % this_y)\n" \
                "       pl.legend(loc=\"best\")\n" \
                "       pl.title(\"Data\")\n" \
                "\ndef gen_pred_fun(clf):\n" \
                "    def pred_fun(x1, x2):\n" \
                "        x = np.array([[x1, x2]])\n" \
                "        return clf.predict(x)[0]\n" \
                "    return pred_fun\n" \
                "\ndef plot_decision_region(X, pred_fun, num):\n" \
                "    min_x = np.min(X[:, 0])\n" \
                "    max_x = np.max(X[:, 0])\n" \
                "    min_y = np.min(X[:, 1])\n" \
                "    max_y = np.max(X[:, 1])\n" \
                "    min_x = min_x - (max_x - min_x) * 0.05\n" \
                "    max_x = max_x + (max_x - min_x) * 0.05\n" \
                "    min_y = min_y - (max_y - min_y) * 0.05\n" \
                "    max_y = max_y + (max_y - min_y) * 0.05\n" \
                "    x_vals = np.linspace(min_x, max_x, num)\n" \
                "    y_vals = np.linspace(min_y, max_y, num)\n" \
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

    ########################################################################################

    tabla = {}

    ayuda ={"datos":"Sirve para cargar los datos.\n"
                    "     Tiene las siguientes sintaxis:\n"
                    "           1. ejemplo STRING (, STRING)?\n "
                    "           2. datos STRING\n"
                    "\n     Ejemplo de uso:\n datosAPredecir = datos \"../datos/misDatos.csv\" \n",

            "asignacion": "Sirve para asignar a un id datos, modelo, metodo, o asignaciones multiples.\n"
                          "    Tiene las siguientes sintaxis:\n"
                          "        1. ID = datos\n"                 
                          "        2. ID = modelo\n"                
                          "        3. ID = metodo\n"                
                          "        4. ID Y ID = division\n"          
                          "\nEjemplo de uso:\n    datosDeEjemplo = ejemplos \"../datos/ejemplos.csv\", \"color\" ",

	        "division": "Sirve para dividir los datos en dos grupos (entrenamineto y prueba) en un porcentaje\n"
                        "NUMERO (asignado a prueba y 1-NUMERO asignado a entrenamiento)\n"
                        "    Tiene las siguientes sintaxis: \n"
                        "        1. dividirDatos ID (: NUMERO)?\n"
                        "\nEjemplo de uso:\n     datosEntrenamiento y datosPrueba = dividirDatos datosDeEjemplo:30\n",

            "modelo": "Asigna el tipo de modelo que se va a utilizar\n"
                      "    Tiene las siguientes sintaxis: \n"
                      "        1. regresionLogistica\n"
                      "        2. bayes\n"
                      "        3. knn\n"
                      "        4. svm\n"
                      "        5. arbolDeDecision\n"
                      "        6. bosqueAleatorio\n"
                      "        7. auto\n"
                      "\nEjemplo de uso:\n miModelo = knn",

             "metodo": "Asigna el metodo a utilizar\n"
                     "      1. entrenamiento\n"
                     "      2. evaluacion\n"
                     "      3. prediccion\n"
                     "      4. reporte\n"
                     "      5. estadisticas\n"
                     "      6. graficas\n"
                     "      7. exportacion\n"
                     "      8. quantil\n"
                     "      9. estandarizacion\n"
                     "      10. escaladominmax\n"
                     "\nEjemplo de uso:\n efectividad = evaluar miModelo con datosPrueba\n",

             "entrenamiento": "Entrena el modelo de primer ID con los datos del segundo ID\n"
                             "      Tiene las siguientes sintaxis:\n"
                             "      1. entrenar ID con ID\n"
                             "\n   Ejemplo de uso:\n miModeloEntrenado = entrenar miModelo con datosEntrenamiento\n",
 
             "evaluacion": "Evalua el modelo de primer ID con los datos del segundo ID\n"
             "      Tiene las siguientes sintaxis:\n"
             "      1. evaluar ID con ID\n"
             "  \nEjemplo de uso:\n miModeloEvaluado = evaluar miModelo con datosEntrenamiento\n",
             
             "prediccion": "Predice el modelo de primer ID con los datos del segundo ID\n"
             "      Tiene las siguientes sintaxis:\n"
             "      1. predecir ID con ID\n"
             "  \nEjemplo de uso:\n miModeloPredicho = predecir miModelo con datosPrueba\n",
 
             "reporte": "Reporta el conjunto de datos de la siguiente manera (filaParaVer,ColumnaParaVer)\n"
             "      Tiene las siguientes sintaxis:\n"
             "      1. reportar ID (NUMERO , NUMERO)?\n"
             "  \nEjemplo de uso:\n reportar dataFrame\n",
 
             "estadisticas":"Muestra las estadisticas del modelo de primer ID con los datos del segundo ID\n"
             "         Tiene las siguientes sintaxis:\n"
             "         1. estadisticas ID con ID\n"
             "  \nEjemplo de uso:\n estadisticas miModelo con datosDeEjemplo\n",
 
             "graficas":" Grafica el modelo de primer ID con los datos de segundo ID y los guarda en la ruta\n"
             "     especificada con el nombre requerido (si no se da una ruta, se guarda en src)\n"
             "         Tiene las siguientes sintaxis:\n"
             "         1. graficar ID con ID (en STRING)? (como STRING (y STRING)?)?\n"
             "  \nEjemplo de uso:\n graficar miModelo con datosDeEjemplo como 'a1' y 'a2'\n",
 
             "exportar":" Exporta el conjunto de datos de primer ID en la ruta\n"
             "         especificada con el nombre requerido (si no se da una ruta, se guarda en src)\n"
             "         Tiene las siguientes sintaxis:\n"
             "         1. exportar ID (en STRING)? (como STRING)?\n"
             "  \nEjemplo de uso:\n exportar dataFrame como 'recetaDeLaSalsaBechamel'\n",

             "quantil": "Subdivide en cuantiles la informacion en un ID de conjunto de datos en una columna STRING\n"
             "         Tiene las siguientes sintaxis:\n"
             "         1. quantil ID STRING\n"
             "\n  Ejemplo de uso:\n quantil dataFrame 'columna'\n",
 
             "estandarizar": "Estadariza la columna STRING del conjunto de datos ID\n"
             "         Tiene las siguientes sintaxis:\n"
             "         1. estandarizar ID STRING\n"
             "\n  Ejemplo de uso:\n estandarizar dataFrame 'columna'\n",
 
             "escaladominmax": "Busca el maximo y minimo valor de la columna STRING de conjunto de datos ID,\n"
             "     al maximo le asigna 1, al minimo 0 y el resto de valores los deja entre 0  y 1\n"
             "     Tiene las siguientes sintaxis:\n"
             "          1. minmax ID STRING\n"
             "\n  Ejemplo de uso:\n minmax dataFrame 'columna'\n",
 
             "codigo_python": "genera (al final) la traduccion del codigo UNa-IA a python\n"
             "     Tiene las siguientes sintaxis:\n"
             "          1. python\n"
             " \n Ejemplo de uso:\n . . . python\n",
 
             "ayuda": "muestra toda la ayuda disponible para las palabras clave\n"
             "     Tiene las siguientes sintaxis:\n"
             "          1. ayuda palabraClave\n"
             "          2. ayuda\n"                      
             "\n  Ejemplo de uso:\n ayuda exportacion \n"
}

    # Visit a parse tree produced by UNaIAParser#ayuda.
    def visitAyuda(self, ctx: UNaIAParser.AyudaContext):
        res = str(ctx.STRING()).replace('"',"")
        if res=="None":
            for k,v in self.ayuda.items():
                print(k,v)
        else:
            if res in self.ayuda:
                print(res,self.ayuda[res])
            else:
                print("La instrucción dada no existe")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by UNaIAParser#codigo_python.
    def visitCodigo_python(self, ctx: UNaIAParser.Codigo_pythonContext):
        self.exportar()
        return self.visitChildren(ctx)

    def exportar(self):
        output_path = "../output/UNaIAModel.py"
        if os.path.exists(output_path):
            os.remove(output_path)

        with open(output_path, "a") as file:
            file.write(self.plantilla)

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
        translation = translator.translate(error_str, src='en', dest='es')
        return translation.text

    def print_error(self, error):
        return self.get_error_translation(self.get_error(str(error)))

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
                           return_times=True, shuffle=True)
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

    # Función para visualizar un conjunto de datos en 2D
    def plot_data(self, X, y):  # Función para graficar datos (X,y)
        y_unique = np.unique(y)
        colors = pl.cm.rainbow(np.linspace(0.0, 1.0, y_unique.size))
        for this_y, color in zip(y_unique, colors):
            this_X = X[y == this_y]
            pl.scatter(this_X[:, 0], this_X[:, 1], c=np.array([color]),
                       alpha=0.5, edgecolor='k',
                       label="Class %s" % this_y)
        pl.legend(loc="best")
        pl.title("Data")

    def gen_pred_fun(self, clf):
        def pred_fun(x1, x2):
            x = np.array([[x1, x2]])
            return clf.predict(x)[0]

        return pred_fun

    # Función para visualizar de la superficie de decisión de un clasificador
    def plot_decision_region(self, X, pred_fun, num):
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

    def visitPrograma(self, ctx: UNaIAParser.ProgramaContext):
        return self.visitChildren(ctx)

        # Visit a parse tree produced by UNaIAParser#datos.

    def visitDatosEjemplos(self, ctx: UNaIAParser.DatosEjemplosContext):
        valor = str(ctx.STRING(1)).replace("\"", "")
        return (str(ctx.STRING(0)).replace('"', ""), valor)

    def visitDatosDatos(self, ctx: UNaIAParser.DatosDatosContext):
        return [str(ctx.STRING()).replace('"', "")]
        # Visit a parse tree produced by UNaIAParser#AsigDatos.

    def visitAsigDatos(self, ctx: UNaIAParser.AsigDatosContext):
        try:
            instruction = ''
            res = self.visit(ctx.datos())
            # print("Voy a revisar los datos: ", res[0])

            if len(res) > 1:
                if res[1] != "None":
                    df = pd.read_csv(res[0])
                    instruction += str(ctx.ID()) + " = pd.read_csv(\"" + str(res[0]) + "\")\n"
                    etiquetas = df[res[1]]
                    instruction += "etiquetas_" + str(ctx.ID()) + " = " + str(ctx.ID()) + '["' + res[1] + '"]\n'
                    caracteristicas = df.drop(res[1], axis=1)
                    instruction += "caracteristicas_" + str(ctx.ID()) + " = " + str(ctx.ID()) + '.drop("' + res[
                        1] + '", axis=1)\n'
                else:
                    df = pd.read_csv(res[0], header=None)
                    instruction += str(ctx.ID()) + " = pd.read_csv(" + str(res[0]) + ", header=None)\n"
                    etiquetas = df.iloc[:, -1]
                    instruction += "etiquetas_" + str(ctx.ID()) + " = " + str(ctx.ID()) + ".iloc[:, -1]\n"
                    caracteristicas = df.iloc[:, :-1]
                    instruction += "caracteristicas_" + str(ctx.ID()) + " = " + str(ctx.ID()) + ".iloc[:, :-1]\n"

                datos_dict = {
                    "etiquetas": etiquetas,
                    "caracteristicas": caracteristicas
                }
                self.tabla[str(ctx.ID())] = datos_dict

            else:

                df = pd.read_csv(res[0])

                if sum(df.columns.str.contains('[A-Za-z]')) > 0:
                    instruction += str(ctx.ID()) + " = pd.read_csv(\"" + str(res[0]) + "\")\n"
                    self.tabla[str(ctx.ID())] = df
                else:
                    instruction += str(ctx.ID()) + " = pd.read_csv(\"" + str(res[0]) + "\", header=None)\n"
                    self.tabla[str(ctx.ID())] = pd.read_csv(res[0], header=None)
            #print(instruction)
            self.plantilla += instruction
        except:
            print("Parece que tienes un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()
        return "Salí de visitAsigDatos"

        # Visit a parse tree produced by UNaIAParser#AsigModelo.

    def visitAsigModelo(self, ctx: UNaIAParser.AsigModeloContext):
        try:
            # Se visita el Nodo modelo y se agraga a la tabla de simbolos
            instruction = ''
            res = self.visit(ctx.modelo())

            if res == 'regresionLogistica':
                modelo = LogisticRegression()
                instruction += str(ctx.ID()) + " = LogisticRegression()\n"
            elif res == 'bayes':
                modelo = GaussianNB()
                instruction += str(ctx.ID()) + " = GaussianNB()\n"
            elif res == 'knn':
                modelo = KNeighborsClassifier(n_neighbors=5)
                instruction += str(ctx.ID()) + " = KNeighborsClassifier(n_neighbors=5)\n"
            elif res == 'svm':
                modelo = sklearn.svm.NuSVC(gamma="auto")
                instruction += str(ctx.ID()) + ' = sklearn.svm.NuSVC(gamma="auto")\n'
            elif res == 'arbolDeDecision':
                modelo = DecisionTreeClassifier()
                instruction += str(ctx.ID()) + " = DecisionTreeClassifier()\n"
            elif res == 'bosqueAleatorio':
                modelo = RandomForestClassifier()
                instruction += str(ctx.ID()) + " = RandomForestClassifier()\n"
            elif res == 'auto':
                modelo = autosklearn.classification.AutoSklearnClassifier(time_left_for_this_task=30)
                instruction += str(
                    ctx.ID()) + " = autosklearn.classification.AutoSklearnClassifier(time_left_for_this_task=30)\n"

            self.tabla[str(ctx.ID())] = modelo

            #print(instruction)
            self.plantilla += instruction
        except:
            print("Parece que tienes un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()
        return "salí de asigModelo"

        # Visit a parse tree produced by UNaIAParser#AsigMetodo.

    def visitAsigMetodo(self, ctx: UNaIAParser.AsigMetodoContext):
        try:
            res = self.visit(ctx.metodo())
            # print("Agrego a la tabla", ctx.ID(), "contienen", res)
            self.tabla[str(ctx.ID())] = res
        except:
            print("Parece que tienes un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()
        return "salí de visitAsigMetodo"

        # Visit a parse tree produced by UNaIAParser#AsigMulti.

    def visitAsigMulti(self, ctx: UNaIAParser.AsigMultiContext):
        try:
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
            # print(len(entrenamiento_dict["etiquetas"]), len(pruebas_dict["etiquetas"]))
        except:
            print("Parece que tienes un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()
        return "Sali de AsigMulti"

        # Visit a parse tree produced by UNaIAParser#division.

    def visitDivision(self, ctx: UNaIAParser.DivisionContext):
        try:
            instruction = ""
            # print(str(ctx.parentCtx.ID(0)))
            # Se deberia verificar que no de menos o mas de uno
            if ctx.NUMERO() == None:
                porcentaje = 30
            else:
                porcentaje = int(str(ctx.NUMERO()))

            if porcentaje > 100 or porcentaje < 0:
                raise Exception("Hubo un error semántico, Los porcentajes asignados para la"
                                " division del dataset, son superior o inferior a 100, Posición: "
                                + str(ctx.start.line) + ", " + str(ctx.getText().find(",") + ctx.start.column + 1))
            else:
                datos = self.tabla[str(ctx.ID())]
                X_train, X_test, y_train, y_test = train_test_split(
                    datos["caracteristicas"], datos["etiquetas"], test_size=porcentaje / 100)

                instruction += "caracteristicas_" + str(ctx.parentCtx.ID(0)) + ", caracteristicas_" + str(ctx.parentCtx.ID(1)) +\
                               ", etiquetas_" + str(ctx.parentCtx.ID(0)) + ", etiquetas_" + str(ctx.parentCtx.ID(1))
                instruction += " = train_test_split(caracteristicas_" + str(ctx.ID()) + ", etiquetas_" + str(
                    ctx.ID()) + ", test_size=" + str(porcentaje / 100) + ")\n"

            #print(instruction)
            self.plantilla += instruction
        except:
            print("Parece que tienes un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()
        return (X_train, y_train), (X_test, y_test)

        # Visit a parse tree produced by UNaIAParser#modelo.

    def visitModelo(self, ctx: UNaIAParser.ModeloContext):

        return ctx.getText()

        # Visit a parse tree produced by UNaIAParser#metodo.

    def visitMetodo(self, ctx: UNaIAParser.MetodoContext):
        return self.visitChildren(ctx)

        # Visit a parse tree produced by UNaIAParser#entrenamiento.

    def visitEntrenamiento(self, ctx: UNaIAParser.EntrenamientoContext):
        try:
            instruction = ''

            datos = self.tabla[str(ctx.ID(1))]
            caracteristicas = datos["caracteristicas"]
            etiquetas = datos["etiquetas"]
            blockPrint()
            self.tabla[str(ctx.ID(0))].fit(caracteristicas, etiquetas)

            instruction += str(ctx.ID(0)) + ".fit(" + "caracteristicas_" + str(ctx.ID(1)) + ", etiquetas_" + str(
                ctx.ID(1)) + ")\n\n"

            enablePrint()
            try:
                print("\n\n#####################################################")
                print("Resultados de la Validación Cruzada para el Modelo", str(ctx.ID(0)), ":\n")

                instruction += 'print("\\n\\n#####################################################")\n'
                instruction += 'print("Resultados de la Validación Cruzada para el Modelo ' + str(ctx.ID(0)) + ' :\\n")\n'

                modl_name = Counter()
                for i in ['mean_test_score', 'mean_fit_time', 'params']:
                    if type(self.tabla[str(ctx.ID(0))].cv_results_[i]) == np.ndarray:
                        lis = self.tabla[str(ctx.ID(0))].cv_results_[i]
                        print(i, sum(lis) / len(lis))

                        instruction += "print(\"" + i + " " + str(sum(lis) / len(lis)) + "\")\n"
                    else:
                        print("\nConteo de modelos entrenados y sus tipos: \n")

                        instruction += 'print("\\nConteo de modelos entrenados y sus tipos: \\n")\n'

                        modl = self.tabla[str(ctx.ID(0))].cv_results_[i]
                        for j in modl:
                            # print(i)
                            modl_name[j["classifier:__choice__"]] += 1

                for i in modl_name:
                    print("Numero de", i, " entrenados:", modl_name[i])
                    instruction += 'print("Numero de ' + str(i) + ' entrenados: ' + str(modl_name[i]) + '")\n'

                print("#####################################################\n\n")
                print("#####################################################")
                print("Resultados de Auto Sklearn para el Modelo", str(ctx.ID(0)), ":\n")

                instruction += 'print("#####################################################\\n\\n")\n'
                instruction += '\nprint("#####################################################")\n'
                instruction += 'print("Resultados de Auto Sklearn para el Modelo ' + str(ctx.ID(0)) + ' :\\n")\n'

                lis = [i.replace("\n", "") for i in self.tabla[str(ctx.ID(0))].sprint_statistics().split("  ")]
                print(lis[2])
                print(lis[3])
                print(lis[4])
                print("#####################################################\n\n")

                instruction += 'print("' + lis[2] + '")\n'
                instruction += 'print("' + lis[3] + '")\n'
                instruction += 'print("' + lis[4] + '")\n'
                instruction += 'print("#####################################################\\n\\n")\n\n'


            except Exception:
                pass

            #print(instruction)
            self.plantilla += instruction
        except:
            print("Parece que hay un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()
        return "Terminado el Entrenamiento"

        # Visit a parse tree produced by UNaIAParser#evaluacion.

    def visitEvaluacion(self, ctx: UNaIAParser.EvaluacionContext):
        try:
            instruction = ""
            datos = self.tabla[str(ctx.ID(1))]
            caracteristicas = datos["caracteristicas"]
            etiquetas = datos["etiquetas"]

            # print(caracteristicas)
            # print(etiquetas)

            res = self.tabla[str(ctx.ID(0))].score(caracteristicas, etiquetas)
            instruction += "desempeño_" + str(ctx.ID(0)) + "= " + str(ctx.ID(0)) + ".score(" + "caracteristicas_" + str(
                ctx.ID(1)) + ", etiquetas_" + str(ctx.ID(1)) + ")\n"
            print("#####################################################")
            print("Desempeño del modelo", str(ctx.ID(0)), ":", res)
            print("#####################################################\n\n")

            instruction += 'print("#####################################################")\n'
            instruction += 'print("Desempeño del modelo ' + str(ctx.ID(0)) + ' :", desempeño_' + str(ctx.ID(0)) + ')\n'
            instruction += 'print("#####################################################\\n\\n")\n'

            #print(instruction)
            self.plantilla += instruction
        except:
            print("Parece que tienes un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()
        return res

        # Visit a parse tree produced by UNaIAParser#prediccion.

    def visitPrediccion(self, ctx: UNaIAParser.PrediccionContext):
        try:
            instruction = ""
            datos = self.tabla[str(ctx.ID(1))]
            predictions = self.tabla[str(ctx.ID(0))].predict(datos)
            # print(self.tabla[str(ctx.ID(0))])
            pruebas_dict = {
                "etiquetas": predictions,
                "caracteristicas": datos
            }
            # print(datos.head())

            instruction += str(ctx.parentCtx.parentCtx.ID()) + " = " + str(ctx.ID(1)) + "\n"
            instruction += "caracteristicas_" + str(ctx.parentCtx.parentCtx.ID()) + " = " + str(ctx.ID(1)) + "\n"
            #instruction += str(ctx.parentCtx.parentCtx.ID()) + "['Etiquetas'] = " + str(ctx.ID(0)) + ".predict(" + str(ctx.ID(1)) + ")\n"
            instruction += "etiquetas_" + str(ctx.parentCtx.parentCtx.ID()) + " = "+ str(ctx.ID(0)) + ".predict(" + str(ctx.ID(1)) + ")\n"
            #print(instruction)
            self.plantilla += instruction
        except:
            print("Parece que tienes un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()
        return pruebas_dict

    # Visit a parse tree produced by UNaIAParser#reporte.
    def visitReporte(self, ctx: UNaIAParser.ReporteContext):
        try:
            instruction = ""
            rows = int(str(ctx.NUMERO(0))) if ctx.NUMERO(0) != None else None
            cols = int(str(ctx.NUMERO(1))) if ctx.NUMERO(1) != None else None

            datos = self.tabla[str(ctx.ID())]

            instruction += "with pd.option_context('display.max_rows', " + str(rows) + ", 'display.max_columns', " + str(
                cols) + "):\n"
            with pd.option_context('display.max_rows', rows, 'display.max_columns', cols):
                print("#####################################################")
                print("Las Caracteristicas la variable son las siguientes: ")
                print(datos["caracteristicas"])
                print("\nSu Análisis Descriptivo es el siguiente: ")
                print(datos["caracteristicas"].describe(include='all'))
                print("#####################################################\n\n")

                instruction += '    print("#####################################################")\n'
                instruction += '    print("Las Caracteristicas de la variable son las siguientes: ")\n'
                instruction += '    print(caracteristicas_' + str(ctx.ID()) + ')\n'
                instruction += '    print("\\nSu Análisis Descriptivo es el siguiente: ")\n'
                instruction += '    print(caracteristicas_' + str(ctx.ID()) + '.describe(include="all"))\n'
                instruction += '    print("#####################################################\\n\\n")\n\n'

                print("#####################################################")
                print("\nLas Etiquetas del DataFrame son las siguientes: ")
                print(datos["etiquetas"])
                print("\nSu Análisis Descriptivo es el siguiente: ")
                print(datos["etiquetas"].describe(include='all'))
                print("#####################################################\n\n")

                instruction += '    print("#####################################################")\n'
                instruction += '    print("\\nLas Etiquetas del DataFrame son las siguientes: ")\n'
                instruction += '    print(etiquetas_' + str(ctx.ID()) + ')\n'
                instruction += '    print("\\nSu Análisis Descriptivo es el siguiente: ")\n'
                instruction += '    print(etiquetas_' + str(ctx.ID()) + '.describe(include="all"))\n'
                instruction += '    print("#####################################################\\n\\n")\n'

            #print(instruction)
            self.plantilla += instruction
        except:
            print("Parece que tienes un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by UNaIAParser#estadisticas.
    def visitEstadisticas(self, ctx: UNaIAParser.EstadisticasContext):
        try:
            datos = self.tabla[str(ctx.ID(1))]

            caracteristicas = datos["caracteristicas"]
            etiquetas = datos["etiquetas"]
            predictions = self.tabla[str(ctx.ID(0))].predict(caracteristicas)

            self.plantilla += "predictions_" + str(ctx.ID(0)) + "= " + str(ctx.ID(0)) + ".predict(caracteristicas_" + str(ctx.ID(1)) + ")\n"

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

            self.plantilla += "\ncnf_matrix_" + str(ctx.ID(0)) + "= confusion_matrix(etiquetas_" + str(ctx.ID(1)) + ", predictions_" + str(ctx.ID(0)) + ")\n" \
                               "print('#####################################################\\n')\n" \
                               "print('Matriz de confusion del modelo, " + str(ctx.ID(0)) + ":\\n')\n" \
                               "print(cnf_matrix_" + str(ctx.ID(0)) + ")\n" \
                               "print('#####################################################\\n\\n')\n\n"\
                               "print('#####################################################\\n')\n"\
                               "print('Resultados del modelo " + str(ctx.ID(0)) + ":\\n')\n" \
                               "print('Precision: {}'.format(metrics.precision_score(etiquetas_" + str(ctx.ID(1)) + ", predictions_" + str(ctx.ID(0)) + ", average='micro')))\n" \
                               "print('Recall: {}'.format(metrics.recall_score(etiquetas_" + str(ctx.ID(1)) + ", predictions_" + str(ctx.ID(0)) + ", average='micro')))\n" \
                               "print('Puntaje F_1: {}'.format(metrics.f1_score(etiquetas_" + str(ctx.ID(1)) + ", predictions_" + str(ctx.ID(0)) + ", average='micro')))\n" \
                               "print('#####################################################\\n\\n')\n"
        except:
            print("Parece que tienes un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()

        return self.visitChildren(ctx)

    # Visit a parse tree produced by UNaIAParser#graficas.
    def visitGraficas(self, ctx: UNaIAParser.GraficasContext):
        try:
            datos = self.tabla[str(ctx.ID(1))]
            #self.plantillas += "datos_" + str(ctx.ID())
            caracteristicas = datos["caracteristicas"]
            etiquetas = datos["etiquetas"]
            #self.plantilla += "\ncaracteristicas_" + str(ctx.ID(1)) + " = datos_" + str(ctx.ID(1)) + "['caracteristicas']\n" \
                          #     "etiquetas_" + str(ctx.ID(1)) + " = datos_" + str(ctx.ID(1)) + "['etiquetas']\n"
            num = 100
            if str(self.tabla[str(ctx.ID(0))])[0:4] == "Auto":
                print("Usted Eligio un Modelo automático, su gráfica se puede demorar, espere por favor: ")
                self.plantilla += "print('Usted Eligio un Modelo automático, su gráfica se puede demorar, espere por favor: ')\n"
                num = 10
            self.plot_decision_region(caracteristicas.values, self.gen_pred_fun(self.tabla[str(ctx.ID(0))]), num)
            self.plantilla += "plot_decision_region(caracteristicas_" + str(ctx.ID(1)) + ".values, " + "gen_pred_fun(" + str(ctx.ID(0)) + "), " + str(num) + ")\n"
            self.plot_data(caracteristicas.values, etiquetas.values)
            self.plantilla += "plot_data(caracteristicas_" + str(ctx.ID(1)) + ".values, " + "etiquetas_" + \
                               str(ctx.ID(1)) + ".values)\n"

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
            self.plantilla += 'pl.title("Region de Decision de ' + str(ctx.ID(0)) + '")\n' \
                               "pl.savefig('" + ruta + "', bbox_inches='tight')\n" \
                               "pl.show()\n\n"
            if str(self.tabla[str(ctx.ID(0))])[0:4] != "Auto":
                self.plot_learning_curve(self.tabla[str(ctx.ID(0))], "Curva de aprendizaje de " + str(ctx.ID(0)),
                                         caracteristicas, etiquetas, axes=None, ylim=None, cv=None)

                self.plantilla += 'plot_learning_curve(' + str(ctx.ID(0)) + ', "Curva de aprendizaje de ' + \
                                  str(ctx.ID(0)) + '", caracteristicas_' + str(ctx.ID(1)) + ', etiquetas_' + str(ctx.ID(1)) + ', axes=None, ylim=None, cv=None)\n'

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
                self.plantilla += "plt.savefig('" + ruta + "', bbox_inches='tight')\n" \
                                                           "plt.show()\n"
        except:
            print("Parece que tienes un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by UNaIAParser#exportacion.
    def visitExportacion(self, ctx: UNaIAParser.ExportacionContext):
        try:
            datos = self.tabla[str(ctx.ID())]

            if type(datos) != pd.core.frame.DataFrame:
                df = datos["caracteristicas"]
                df["Etiquetas"] = datos["etiquetas"]
                self.plantilla += "df_" + str(ctx.ID()) + " = caracteristicas_" + str(ctx.ID()) + "\n" \
                                 "df_" + str(ctx.ID()) + "['Etiquetas'] = etiquetas_" + str(ctx.ID()) + "\n"
            else:
                df = datos
                self.plantilla += "df_" + str(ctx.ID()) + " = " + str(ctx.ID()) + "\n"

            ruta = ""
            nombre = str(ctx.ID()) + '.csv'

            if ctx.EN() != None:
                ruta += str(ctx.STRING(0)).replace('"', "") + '/'
                if ctx.COMO() != None:
                    nombre = str(ctx.STRING(1)).replace('"', "") + ".csv"
            elif ctx.COMO() != None:
                nombre = str(ctx.STRING(0)).replace('"', "") + ".csv"

            ruta += nombre
            df.to_csv(ruta, index=False)
            self.plantilla += "df_" + str(ctx.ID()) + ".to_csv('" + ruta + "', index=False)\n"
        except:
            print("Parece que tienes un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by UNaIAParser#normalizacion.
    def visitQuantil(self, ctx: UNaIAParser.QuantilContext):
        try:
            datos = self.tabla[str(ctx.ID())]
            datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")] = datos["caracteristicas"][
                str(ctx.STRING()).replace("\"", "")].values.astype(float)
            q_scale = preprocessing.QuantileTransformer()
            col_scaled = q_scale.fit_transform(
                datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")].values.reshape(-1, 1))
            datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")] = col_scaled

            self.plantilla += "\ncaracteristicas_" + str(ctx.ID()) + "[" + str(ctx.STRING()) + "]" \
                              " = caracteristicas_" + str(ctx.ID()) + "[" + str(ctx.STRING()) + "].values.astype(float)\n" \
                            "q_scale = preprocessing.QuantileTransformer()\n" \
                            "col_scaled = q_scale.fit_transform(caracteristicas_" + str(ctx.ID()) + "[" \
                              + str(ctx.STRING()) + "].values.reshape(-1, 1))\n" \
                                                                      "caracteristicas_" + str(ctx.ID()) + "[" + str(ctx.STRING()) + "] = col_scaled\n"

            self.tabla[str(ctx.ID())] = datos
        except:
            print("Parece que tienes un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()
        return "Ha sido Normalizado Correctamente"

    # Visit a parse tree produced by UNaIAParser#estandarizacion.
    def visitEstandarizacion(self, ctx: UNaIAParser.EstandarizacionContext):
        try:
            datos = self.tabla[str(ctx.ID())]
            datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")] = datos["caracteristicas"][
                str(ctx.STRING()).replace("\"", "")].values.astype(float)
            std_scaler = preprocessing.StandardScaler()
            col_scaled = std_scaler.fit_transform(
                datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")].values.reshape(-1, 1))
            datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")] = col_scaled

            self.plantilla += "\ncaracteristicas_" + str(ctx.ID()) + "[" + str(ctx.STRING()) + "]" \
                            " = caracteristicas_" + str(ctx.ID()) + "[" + str(ctx.STRING()) + "].values.astype(float)\n" \
                            "std_scaler = preprocessing.StandardScaler()\n" \
                            "col_scaled = std_scaler.fit_transform(caracteristicas_" + str(ctx.ID()) + "[" \
                              + str(ctx.STRING())+ "].values.reshape(-1, 1))\n" \
                                "caracteristicas_" + str(ctx.ID()) + "[" + str(ctx.STRING()) + "] = col_scaled\n"

            self.tabla[str(ctx.ID())] = datos
        except:
            print("Parece que tienes un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()
        return "Ha sido Estandarizado correctamente"

    # Visit a parse tree produced by UNaIAParser#escaladominmax.
    def visitEscaladominmax(self, ctx: UNaIAParser.EscaladominmaxContext):
        try:
            datos = self.tabla[str(ctx.ID())]

            datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")] = datos["caracteristicas"][
                str(ctx.STRING()).replace("\"", "")].values.astype(float)
            min_max_scaler = preprocessing.MinMaxScaler()
            col_scaled = min_max_scaler.fit_transform(
                datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")].values.reshape(-1, 1))
            datos["caracteristicas"][str(ctx.STRING()).replace("\"", "")] = col_scaled
            self.plantilla += "\ncaracteristicas_" + str(ctx.ID()) + "[" + str(ctx.STRING()) + "]" \
                             " = caracteristicas_" + str(ctx.ID()) + "[" + str(ctx.STRING()) + "].values.astype(float)\n" \
                            "min_max_scaler = preprocessing.MinMaxScaler()\n" \
                            "col_scaled = min_max_scaler.fit_transform(caracteristicas_" + str(ctx.ID()) + "[" \
                              + str(ctx.STRING()) + "].values.reshape(-1, 1))\n" \
                            "caracteristicas_" + str(ctx.ID()) + "[" + str(ctx.STRING()) + "] = col_scaled\n"

            self.tabla[str(ctx.ID())] = datos
        except:
            print("Parece que tienes un error en la línea "+str(ctx.start.line)+": ", self.get_error_translation(self.get_error(str(sys.exc_info()[0]))))
            print("Para más información utilice el comando ayuda <palabraClave>")
            exit()
        return "Ha sido Escalado Correctamente"


del UNaIAParser
