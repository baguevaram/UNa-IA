grammar UNaIA;

// REGLAS SINTACTICAS

programa : (asignacion | metodo)*;

//El archivo de datos a cargar debe ser un csv de la forma datos, Etiqueta
datos: EJEMPLOS STRING (COMA STRING)? #DatosEjemplos
       | DATOS STRING #DatosDatos;


asignacion : ID ASIG datos                 #AsigDatos
            |ID ASIG modelo                #AsigModelo
            |ID ASIG metodo                #AsigMetodo
            |ID Y ID ASIG division      #AsigMulti
            ;

division: DIVIDIRDATOS ID (DOS_PUNTOS NUMERO)?;

modelo: (REGRESIONLOGISTICA |
            BAYES|
            KNN|
            SVM|
            ARBOLDEDESICION|
            BOSQUEALEATORIO|
            AUTO);

metodo: entrenamiento | evaluacion | prediccion | reporte | estadisticas | graficas | exportacion;

entrenamiento: ENTRENAR ID CON ID;

evaluacion: EVALUAR ID CON ID;

prediccion: PREDECIR ID CON ID;

reporte: REPORTAR ID PAR_IZQ (NUMERO COMA NUMERO)? PAR_DER;

estadisticas: ESTADISTICAS ID CON ID;

graficas: GRAFICAR ID CON ID;

exportacion: EXPORTAR ID (EN STRING)? (COMO STRING)?;
// TOKENS

COMMENT
 : '#' ~[\r\n\f]* -> channel(HIDDEN)
 ;

//-------------Palabras reservadas
EJEMPLOS : 'ejemplos';

DATOS : 'datos';

ESTADISTICAS: 'estadisticas';

GRAFICAR:'graficar';

EXPORTAR:'exportar';

ENTRENAR: 'entrenar';

EVALUAR: 'evaluar';

PREDECIR: 'predecir';

DIVIDIRDATOS: 'dividirDatos';

CON: 'con';

Y: 'y';

EN: 'en';

COMO: 'como';

REPORTAR: 'reportar';

REGRESIONLOGISTICA: 'regresionLogistica';

BAYES: 'bayes' ;

KNN: 'knn';

SVM: 'svm';

ARBOLDEDESICION: 'arbolDeDecision';

BOSQUEALEATORIO: 'bosqueAleatorio';

AUTO: 'auto';

//------------Símbolos

COMA:',';

DOS_PUNTOS: ':';

ASIG:'=';

PAR_IZQ: '(';

PAR_DER: ')';

//-----------Tipos

ID: ([A-Z]|[a-z]|'_')([0-9]|[a-z]|[A-Z]|'_')*;

STRING: ('"' ([ -!#-[\]-~] | '\\"' | '\\n' | '\\t' | '\\\\')* '"');

NUMERO: [1-9][0-9]*|'0' ;

//----------Ignorar
ESPACIO:   ( ' '
        | '\t'
        | '\r'
        | '\n'
        )+ -> channel(HIDDEN)
    ;