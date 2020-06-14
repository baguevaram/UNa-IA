grammar UNaIA;

// REGLAS SINTACTICAS
expr	:	term ( (MAS | MENOS) term)*;

term	:	factor ( (MULT | DIV) factor)*;

factor	:	ENTERO;


// TOKENS
MAS 	:	'+';
MENOS 	:	'-';
MULT 	:	'*';
DIV 	:	'/';

// REGLAS LEXICAS
ENTERO :'0'..'9'+;

ESPACIO:   ( ' '
        | '\t'
        | '\r'
        | '\n'
        )+ -> channel(HIDDEN)
    ;

