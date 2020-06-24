# UNa-IA - Proyecto final de Lenguajes de Programación UNAL 2020-1
## Integrantes:
    * Brayan Andrés Guevara Márquez
    * Juan Jesús Pulido Sánchez
    * Oscar Camilo Pulido Peña 
   
* UNa-IA es un lenguaje de dominio específico enfocado a Inteligencia Artificial.

* Este lenguaje tiene sintaxis en español y utiliza los modulos de scikitlearn en\
  Python para ejecutar el código que ingresa el usuario.
  
## ¿Cómo utilizar UNa-IA?

### Contenido del paquete:

* El código está dividido en un archivo README.md y otro llamado requirements.txt, junto con las siguientes carpetas : 
  * datos: Esta carpeta contiene los datos de ejemplo para el uso de UNa-IA; por defecto 
            están los datos del dataset de iris, pero el usuario puede colocar
            acá su conjunto de datos de interés. La carpeta viene con cuatro archivos: 
       * iris.csv
       * iris2.csv
       * testDatos.csv
       * testLogistic.csv
      
  * gen: Contiene los scripts generados por Antlr para el analizados léxico y sintáctico del 
         lenguaje dada la gramática definida
  * Grammar: Contiene un archivo UNaIA.g4 que contiene las reglas de la gramática del lenguaje
  * input: Contiene un archivo llamado in.txt, acá el usuario pondría el código fuente
           en el lenguaje para ser ejecutado posteriormente
  * output: Aquí se generará un archivo llamado UNaIAModel.py, que corresponde
            al archivo de python traducido a partir de el input del usuario en lenguaje
            UNa-IA
  * src: Contiene dos archivos: main.py y MyVisitor.py . El primero ejecuta la lógica general
         de UNa-IA y el segundo es donde se encuentra la lógica del interprete de UNa-IA y traductor 
         a Python.         
### Instrucciones de uso:
1. Abrir el código en su editor de preferencia (Preferiblemente PyCharm)
2. Instalar los paquetes contenidos en requirements.txt
3. Si desea cambiar los conjuntos de datos con los que se va a trabajar: cambiar
   los archivos en la carpeta output
4. Ingresar el código en el archivo in.txt de la carpeta input
5. Ejecutar el script main.py de la carpeta src, asegurarse que tanto las carpetas gen como src 
   sean marcadas como de código fuente.
6. Los resultados del código serán mostrados en consola, así como si se generan imagenes, se guardarán
   en la ruta especificada o por defecto en src
7. En la carpeta output se encontrará el archivo UNaIAModel.py, el cual es la traducción
   del lenguaje de UNaIA a Python para fines académicos (esto sirve cuando se pone el comando python al final del script).
   
TODO:

Entre Todos
    
Camilo (Reunion con Laura Mañana Lunes)
1) Python Code Translate
2) Errors
3) Comando Help

Entrega:

Hacer despues de Revision con Laura
- Ejemplos de Uso (Entrada y Salida)
- README.txt: breve manual de compilación y uso
- Exposición