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


def plot_learning_curve(estimator, title, X, y, axes=None, ylim=None, cv=None,
                         n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
    if axes is None:
        _, axes = plt.subplots(1, 1)
    axes.set_title(title)
    if ylim is not None:
        axes.set_ylim(*ylim)
    axes.set_xlabel("Ejemplos de Entrenamiento")
    axes.set_ylabel("Puntaje")
    train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs,
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

# Función para visualizar un conjunto de datos en 2D
def plot_data(X, y):  # Función para graficar datos (X,y)
   y_unique = np.unique(y)
   colors = pl.cm.rainbow(np.linspace(0.0, 1.0, y_unique.size))
   for this_y, color in zip(y_unique, colors):
       this_X = X[y == this_y]
       pl.scatter(this_X[:, 0], this_X[:, 1], c=np.array([color]),
       alpha=0.5, edgecolor='k',
       label="Class %s" % this_y)
       pl.legend(loc="best")
       pl.title("Data")

def gen_pred_fun(clf):
    def pred_fun(x1, x2):
        x = np.array([[x1, x2]])
        return clf.predict(x)[0]
    return pred_fun

def plot_decision_region(X, pred_fun, num):
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


datosDeEjemplo = pd.read_csv("../datos/testLogistic.csv")
etiquetas_datosDeEjemplo = datosDeEjemplo["label"]
caracteristicas_datosDeEjemplo = datosDeEjemplo.drop("label", axis=1)

caracteristicas_datosDeEjemplo["x"] = caracteristicas_datosDeEjemplo["x"].values.astype(float)
std_scaler = preprocessing.StandardScaler()
col_scaled = std_scaler.fit_transform(caracteristicas_datosDeEjemplo["x"].values.reshape(-1, 1))
caracteristicas_datosDeEjemplo["x"] = col_scaled

caracteristicas_datosDeEjemplo["y"] = caracteristicas_datosDeEjemplo["y"].values.astype(float)
std_scaler = preprocessing.StandardScaler()
col_scaled = std_scaler.fit_transform(caracteristicas_datosDeEjemplo["y"].values.reshape(-1, 1))
caracteristicas_datosDeEjemplo["y"] = col_scaled
with pd.option_context('display.max_rows', 10, 'display.max_columns', 2):
    print("#####################################################")
    print("Las Caracteristicas de la variable son las siguientes: ")
    print(caracteristicas_datosDeEjemplo)
    print("\nSu Análisis Descriptivo es el siguiente: ")
    print(caracteristicas_datosDeEjemplo.describe(include="all"))
    print("#####################################################\n\n")

    print("#####################################################")
    print("\nLas Etiquetas del DataFrame son las siguientes: ")
    print(etiquetas_datosDeEjemplo)
    print("\nSu Análisis Descriptivo es el siguiente: ")
    print(etiquetas_datosDeEjemplo.describe(include="all"))
    print("#####################################################\n\n")
datosAPredecir = pd.read_csv("../datos/testDatos.csv", header=None)
miModelo = DecisionTreeClassifier()
caracteristicas_datosEntrenamiento, caracteristicas_datosPrueba, etiquetas_datosEntrenamiento, etiquetas_datosPrueba = train_test_split(caracteristicas_datosDeEjemplo, etiquetas_datosDeEjemplo, test_size=0.3)
miModelo.fit(caracteristicas_datosEntrenamiento, etiquetas_datosEntrenamiento)

print("\n\n#####################################################")
print("Resultados de la Validación Cruzada para el Modelo miModelo :\n")
datosPredicciones = datosAPredecir
datosPredicciones['Etiquetas'] = miModelo.predict(datosAPredecir)
desempeño_miModelo= miModelo.score(caracteristicas_datosPrueba, etiquetas_datosPrueba)
print("#####################################################")
print("Desempeño del modelo miModelo :", desempeño_miModelo)
print("#####################################################\n\n")
predictions_miModelo= miModelo.predict(caracteristicas_datosDeEjemplo)

cnf_matrix_miModelo= confusion_matrix(etiquetas_datosDeEjemplo, predictions_miModelo)
print('#####################################################\n')
print('Matriz de confusion del modelo, miModelo:\n')
print(cnf_matrix_miModelo)
print('#####################################################\n\n')

print('#####################################################\n')
print('Resultados del modelo miModelo:\n')
print('Precision: {}'.format(metrics.precision_score(etiquetas_datosDeEjemplo, predictions_miModelo, average='micro')))
print('Recall: {}'.format(metrics.recall_score(etiquetas_datosDeEjemplo, predictions_miModelo, average='micro')))
print('Puntaje F_1: {}'.format(metrics.f1_score(etiquetas_datosDeEjemplo, predictions_miModelo, average='micro')))
print('#####################################################\n\n')
plot_decision_region(caracteristicas_datosDeEjemplo.values, gen_pred_fun(miModelo), 100)
plot_data(caracteristicas_datosDeEjemplo.values, etiquetas_datosDeEjemplo.values)
pl.title("Region de Decision de miModelo")
pl.savefig('a1.jpg', bbox_inches='tight')
pl.show()

plot_learning_curve(miModelo, "Curva de aprendizaje de miModelo", caracteristicas_datosDeEjemplo, etiquetas_datosDeEjemplo, axes=None, ylim=None, cv=None)
plt.savefig('a2.jpg', bbox_inches='tight')
plt.show()
df_datosPredicciones = datosPredicciones
df_datosPredicciones.to_csv('datosPredicciones.csv', index=False)
