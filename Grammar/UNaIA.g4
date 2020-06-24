grammar UNaIA;

// REGLAS SINTACTICAS

programa : (asignacion | metodo | ayuda)* (codigo_python)?;

ayuda: AYUDA (STRING)?;

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
            ARBOLDEDECISION|
            BOSQUEALEATORIO|
            AUTO);

metodo: entrenamiento
        | evaluacion
        | prediccion
        | reporte
        | estadisticas
        | graficas
        | exportacion
        | quantil
        | estandarizacion
        | escaladominmax;

entrenamiento: ENTRENAR ID CON ID;

evaluacion: EVALUAR ID CON ID;

prediccion: PREDECIR ID CON ID;

reporte: REPORTAR ID ( PAR_IZQ NUMERO COMA NUMERO PAR_DER)?;

estadisticas: ESTADISTICAS ID CON ID;

graficas: GRAFICAR ID CON ID (EN STRING)? (COMO STRING (Y STRING)?)?;

exportacion: EXPORTAR ID (EN STRING)? (COMO STRING)?;

quantil: QUANTIL ID STRING;

estandarizacion: ESTANDARIZAR ID STRING;

escaladominmax: MINMAX ID STRING;

codigo_python: PYTHON;

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

AYUDA: 'ayuda';

EVALUAR: 'evaluar';

PREDECIR: 'predecir';

DIVIDIRDATOS: 'dividirDatos';

CON: 'con';

Y: 'y';

EN: 'en';

COMO: 'como';

REPORTAR: 'reportar';

QUANTIL: 'quantil';

ESTANDARIZAR: 'estandarizar';

MINMAX: 'minmax';

REGRESIONLOGISTICA: 'regresionLogistica';

BAYES: 'bayes' ;

KNN: 'knn';

SVM: 'svm';

ARBOLDEDECISION: 'arbolDeDecision';

BOSQUEALEATORIO: 'bosqueAleatorio';

AUTO: 'auto';

PYTHON: 'python';

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