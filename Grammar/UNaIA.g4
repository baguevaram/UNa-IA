grammar UNaIA;

// REGLAS SINTACTICAS

programa : (asignacion | metodo)*;

//El archivo de datos a cargar debe ser un csv de la forma datos, Etiqueta
datos: CARGAR PAR_IZQ STRING PAR_DER ;

asignacion : ID ASIG datos                 #AsigDatos
            |ID ASIG modelo                #AsigModelo
            |ID ASIG metodo                #AsigMetodo
            |ID COMA ID ASIG division      #AsigMulti
            ;

division: DIVIDIRDATOS PAR_IZQ ID (COMA NUMERO COMA NUMERO)? PAR_DER;

modelo: (REGRESIONLOGISTICA |
            BAYES|
            KNN|
            SVM|
            ARBOLDEDESICION|
            BOSQUEALEATORIO);

metodo: entrenamiento | evaluacion | prediccion;

entrenamiento: ID PUNTO ENTRENAR PAR_IZQ ID PAR_DER ;

evaluacion: ID PUNTO EVALUAR PAR_IZQ ID PAR_DER;

prediccion: ID PUNTO PREDECIR PAR_IZQ ID PAR_DER;


// TOKENS

COMMENT
 : '#' ~[\r\n\f]* -> channel(HIDDEN)
 ;

//-------------Palabras reservadas
CARGAR : 'cargar';

ENTRENAR: 'entrenar';

EVALUAR: 'evaluar';

PREDECIR: 'predecir';

DIVIDIRDATOS: 'dividirDatos';

REGRESIONLOGISTICA: 'regresionLogistica';

BAYES: 'bayes' ;

KNN: 'knn';

SVM: 'svm';

ARBOLDEDESICION: 'arbolDeDesicion';

BOSQUEALEATORIO: 'bosqueAleatorio';

//------------Símbolos

COMA:',';

PUNTO :'.';

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

