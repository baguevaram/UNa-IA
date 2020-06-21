# Generated from /home/minorin/Documents/UNa-IA/Grammar/UNaIA.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("p\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\7\2\35\n\2\f\2\16\2 \13\2\3\3\3\3\3\3\3\3\5\3&\n\3\3")
        buf.write("\3\3\3\5\3*\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\5\4:\n\4\3\5\3\5\3\5\3\5\5\5@\n\5\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7J\n\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\5\13b\n\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\2\2\16\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\2\3\3\2\16\24\2q\2\36\3\2\2\2")
        buf.write("\4)\3\2\2\2\69\3\2\2\2\b;\3\2\2\2\nA\3\2\2\2\fI\3\2\2")
        buf.write("\2\16K\3\2\2\2\20P\3\2\2\2\22U\3\2\2\2\24Z\3\2\2\2\26")
        buf.write("e\3\2\2\2\30j\3\2\2\2\32\35\5\6\4\2\33\35\5\f\7\2\34\32")
        buf.write("\3\2\2\2\34\33\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37")
        buf.write("\3\2\2\2\37\3\3\2\2\2 \36\3\2\2\2!\"\7\4\2\2\"%\7\35\2")
        buf.write("\2#$\7\25\2\2$&\7\35\2\2%#\3\2\2\2%&\3\2\2\2&*\3\2\2\2")
        buf.write("\'(\7\5\2\2(*\7\35\2\2)!\3\2\2\2)\'\3\2\2\2*\5\3\2\2\2")
        buf.write("+,\7\34\2\2,-\7\30\2\2-:\5\4\3\2./\7\34\2\2/\60\7\30\2")
        buf.write("\2\60:\5\n\6\2\61\62\7\34\2\2\62\63\7\30\2\2\63:\5\f\7")
        buf.write("\2\64\65\7\34\2\2\65\66\7\33\2\2\66\67\7\34\2\2\678\7")
        buf.write("\30\2\28:\5\b\5\29+\3\2\2\29.\3\2\2\29\61\3\2\2\29\64")
        buf.write("\3\2\2\2:\7\3\2\2\2;<\7\13\2\2<?\7\34\2\2=>\7\26\2\2>")
        buf.write("@\7\36\2\2?=\3\2\2\2?@\3\2\2\2@\t\3\2\2\2AB\t\2\2\2B\13")
        buf.write("\3\2\2\2CJ\5\16\b\2DJ\5\20\t\2EJ\5\22\n\2FJ\5\24\13\2")
        buf.write("GJ\5\26\f\2HJ\5\30\r\2IC\3\2\2\2ID\3\2\2\2IE\3\2\2\2I")
        buf.write("F\3\2\2\2IG\3\2\2\2IH\3\2\2\2J\r\3\2\2\2KL\7\b\2\2LM\7")
        buf.write("\34\2\2MN\7\f\2\2NO\7\34\2\2O\17\3\2\2\2PQ\7\t\2\2QR\7")
        buf.write("\34\2\2RS\7\f\2\2ST\7\34\2\2T\21\3\2\2\2UV\7\n\2\2VW\7")
        buf.write("\34\2\2WX\7\f\2\2XY\7\34\2\2Y\23\3\2\2\2Z[\7\r\2\2[\\")
        buf.write("\7\34\2\2\\a\7\31\2\2]^\7\25\2\2^_\7\36\2\2_`\7\25\2\2")
        buf.write("`b\7\36\2\2a]\3\2\2\2ab\3\2\2\2bc\3\2\2\2cd\7\32\2\2d")
        buf.write("\25\3\2\2\2ef\7\6\2\2fg\7\34\2\2gh\7\f\2\2hi\7\34\2\2")
        buf.write("i\27\3\2\2\2jk\7\7\2\2kl\7\34\2\2lm\7\f\2\2mn\7\34\2\2")
        buf.write("n\31\3\2\2\2\n\34\36%)9?Ia")
        return buf.getvalue()


class UNaIAParser ( Parser ):

    grammarFileName = "UNaIA.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'ejemplos'", "'datos'", 
                     "'estadisticas'", "'graficar'", "'entrenar'", "'evaluar'", 
                     "'predecir'", "'dividirDatos'", "'con'", "'reportar'", 
                     "'regresionLogistica'", "'bayes'", "'knn'", "'svm'", 
                     "'arbolDeDecision'", "'bosqueAleatorio'", "'auto'", 
                     "','", "':'", "'.'", "'='", "'('", "')'", "'y'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "EJEMPLOS", "DATOS", "ESTADISTICAS", 
                      "GRAFICAR", "ENTRENAR", "EVALUAR", "PREDECIR", "DIVIDIRDATOS", 
                      "CON", "REPORTAR", "REGRESIONLOGISTICA", "BAYES", 
                      "KNN", "SVM", "ARBOLDEDESICION", "BOSQUEALEATORIO", 
                      "AUTO", "COMA", "DOS_PUNTOS", "PUNTO", "ASIG", "PAR_IZQ", 
                      "PAR_DER", "Y", "ID", "STRING", "NUMERO", "ESPACIO" ]

    RULE_programa = 0
    RULE_datos = 1
    RULE_asignacion = 2
    RULE_division = 3
    RULE_modelo = 4
    RULE_metodo = 5
    RULE_entrenamiento = 6
    RULE_evaluacion = 7
    RULE_prediccion = 8
    RULE_reporte = 9
    RULE_estadisticas = 10
    RULE_graficas = 11

    ruleNames =  [ "programa", "datos", "asignacion", "division", "modelo", 
                   "metodo", "entrenamiento", "evaluacion", "prediccion", 
                   "reporte", "estadisticas", "graficas" ]

    EOF = Token.EOF
    COMMENT=1
    EJEMPLOS=2
    DATOS=3
    ESTADISTICAS=4
    GRAFICAR=5
    ENTRENAR=6
    EVALUAR=7
    PREDECIR=8
    DIVIDIRDATOS=9
    CON=10
    REPORTAR=11
    REGRESIONLOGISTICA=12
    BAYES=13
    KNN=14
    SVM=15
    ARBOLDEDESICION=16
    BOSQUEALEATORIO=17
    AUTO=18
    COMA=19
    DOS_PUNTOS=20
    PUNTO=21
    ASIG=22
    PAR_IZQ=23
    PAR_DER=24
    Y=25
    ID=26
    STRING=27
    NUMERO=28
    ESPACIO=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UNaIAParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(UNaIAParser.AsignacionContext,i)


        def metodo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UNaIAParser.MetodoContext)
            else:
                return self.getTypedRuleContext(UNaIAParser.MetodoContext,i)


        def getRuleIndex(self):
            return UNaIAParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = UNaIAParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << UNaIAParser.ESTADISTICAS) | (1 << UNaIAParser.GRAFICAR) | (1 << UNaIAParser.ENTRENAR) | (1 << UNaIAParser.EVALUAR) | (1 << UNaIAParser.PREDECIR) | (1 << UNaIAParser.REPORTAR) | (1 << UNaIAParser.ID))) != 0):
                self.state = 26
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [UNaIAParser.ID]:
                    self.state = 24
                    self.asignacion()
                    pass
                elif token in [UNaIAParser.ESTADISTICAS, UNaIAParser.GRAFICAR, UNaIAParser.ENTRENAR, UNaIAParser.EVALUAR, UNaIAParser.PREDECIR, UNaIAParser.REPORTAR]:
                    self.state = 25
                    self.metodo()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return UNaIAParser.RULE_datos

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DatosDatosContext(DatosContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UNaIAParser.DatosContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DATOS(self):
            return self.getToken(UNaIAParser.DATOS, 0)
        def STRING(self):
            return self.getToken(UNaIAParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDatosDatos" ):
                listener.enterDatosDatos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDatosDatos" ):
                listener.exitDatosDatos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDatosDatos" ):
                return visitor.visitDatosDatos(self)
            else:
                return visitor.visitChildren(self)


    class DatosEjemplosContext(DatosContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UNaIAParser.DatosContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EJEMPLOS(self):
            return self.getToken(UNaIAParser.EJEMPLOS, 0)
        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.STRING)
            else:
                return self.getToken(UNaIAParser.STRING, i)
        def COMA(self):
            return self.getToken(UNaIAParser.COMA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDatosEjemplos" ):
                listener.enterDatosEjemplos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDatosEjemplos" ):
                listener.exitDatosEjemplos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDatosEjemplos" ):
                return visitor.visitDatosEjemplos(self)
            else:
                return visitor.visitChildren(self)



    def datos(self):

        localctx = UNaIAParser.DatosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_datos)
        self._la = 0 # Token type
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [UNaIAParser.EJEMPLOS]:
                localctx = UNaIAParser.DatosEjemplosContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(UNaIAParser.EJEMPLOS)
                self.state = 32
                self.match(UNaIAParser.STRING)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==UNaIAParser.COMA:
                    self.state = 33
                    self.match(UNaIAParser.COMA)
                    self.state = 34
                    self.match(UNaIAParser.STRING)


                pass
            elif token in [UNaIAParser.DATOS]:
                localctx = UNaIAParser.DatosDatosContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(UNaIAParser.DATOS)
                self.state = 38
                self.match(UNaIAParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return UNaIAParser.RULE_asignacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsigMetodoContext(AsignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UNaIAParser.AsignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(UNaIAParser.ID, 0)
        def ASIG(self):
            return self.getToken(UNaIAParser.ASIG, 0)
        def metodo(self):
            return self.getTypedRuleContext(UNaIAParser.MetodoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsigMetodo" ):
                listener.enterAsigMetodo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsigMetodo" ):
                listener.exitAsigMetodo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsigMetodo" ):
                return visitor.visitAsigMetodo(self)
            else:
                return visitor.visitChildren(self)


    class AsigMultiContext(AsignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UNaIAParser.AsignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.ID)
            else:
                return self.getToken(UNaIAParser.ID, i)
        def Y(self):
            return self.getToken(UNaIAParser.Y, 0)
        def ASIG(self):
            return self.getToken(UNaIAParser.ASIG, 0)
        def division(self):
            return self.getTypedRuleContext(UNaIAParser.DivisionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsigMulti" ):
                listener.enterAsigMulti(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsigMulti" ):
                listener.exitAsigMulti(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsigMulti" ):
                return visitor.visitAsigMulti(self)
            else:
                return visitor.visitChildren(self)


    class AsigModeloContext(AsignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UNaIAParser.AsignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(UNaIAParser.ID, 0)
        def ASIG(self):
            return self.getToken(UNaIAParser.ASIG, 0)
        def modelo(self):
            return self.getTypedRuleContext(UNaIAParser.ModeloContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsigModelo" ):
                listener.enterAsigModelo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsigModelo" ):
                listener.exitAsigModelo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsigModelo" ):
                return visitor.visitAsigModelo(self)
            else:
                return visitor.visitChildren(self)


    class AsigDatosContext(AsignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a UNaIAParser.AsignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(UNaIAParser.ID, 0)
        def ASIG(self):
            return self.getToken(UNaIAParser.ASIG, 0)
        def datos(self):
            return self.getTypedRuleContext(UNaIAParser.DatosContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsigDatos" ):
                listener.enterAsigDatos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsigDatos" ):
                listener.exitAsigDatos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsigDatos" ):
                return visitor.visitAsigDatos(self)
            else:
                return visitor.visitChildren(self)



    def asignacion(self):

        localctx = UNaIAParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asignacion)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = UNaIAParser.AsigDatosContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(UNaIAParser.ID)
                self.state = 42
                self.match(UNaIAParser.ASIG)
                self.state = 43
                self.datos()
                pass

            elif la_ == 2:
                localctx = UNaIAParser.AsigModeloContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(UNaIAParser.ID)
                self.state = 45
                self.match(UNaIAParser.ASIG)
                self.state = 46
                self.modelo()
                pass

            elif la_ == 3:
                localctx = UNaIAParser.AsigMetodoContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.match(UNaIAParser.ID)
                self.state = 48
                self.match(UNaIAParser.ASIG)
                self.state = 49
                self.metodo()
                pass

            elif la_ == 4:
                localctx = UNaIAParser.AsigMultiContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.match(UNaIAParser.ID)
                self.state = 51
                self.match(UNaIAParser.Y)
                self.state = 52
                self.match(UNaIAParser.ID)
                self.state = 53
                self.match(UNaIAParser.ASIG)
                self.state = 54
                self.division()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DivisionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIVIDIRDATOS(self):
            return self.getToken(UNaIAParser.DIVIDIRDATOS, 0)

        def ID(self):
            return self.getToken(UNaIAParser.ID, 0)

        def DOS_PUNTOS(self):
            return self.getToken(UNaIAParser.DOS_PUNTOS, 0)

        def NUMERO(self):
            return self.getToken(UNaIAParser.NUMERO, 0)

        def getRuleIndex(self):
            return UNaIAParser.RULE_division

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivision" ):
                listener.enterDivision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivision" ):
                listener.exitDivision(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivision" ):
                return visitor.visitDivision(self)
            else:
                return visitor.visitChildren(self)




    def division(self):

        localctx = UNaIAParser.DivisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_division)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(UNaIAParser.DIVIDIRDATOS)
            self.state = 58
            self.match(UNaIAParser.ID)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==UNaIAParser.DOS_PUNTOS:
                self.state = 59
                self.match(UNaIAParser.DOS_PUNTOS)
                self.state = 60
                self.match(UNaIAParser.NUMERO)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModeloContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REGRESIONLOGISTICA(self):
            return self.getToken(UNaIAParser.REGRESIONLOGISTICA, 0)

        def BAYES(self):
            return self.getToken(UNaIAParser.BAYES, 0)

        def KNN(self):
            return self.getToken(UNaIAParser.KNN, 0)

        def SVM(self):
            return self.getToken(UNaIAParser.SVM, 0)

        def ARBOLDEDESICION(self):
            return self.getToken(UNaIAParser.ARBOLDEDESICION, 0)

        def BOSQUEALEATORIO(self):
            return self.getToken(UNaIAParser.BOSQUEALEATORIO, 0)

        def AUTO(self):
            return self.getToken(UNaIAParser.AUTO, 0)

        def getRuleIndex(self):
            return UNaIAParser.RULE_modelo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelo" ):
                listener.enterModelo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelo" ):
                listener.exitModelo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelo" ):
                return visitor.visitModelo(self)
            else:
                return visitor.visitChildren(self)




    def modelo(self):

        localctx = UNaIAParser.ModeloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_modelo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << UNaIAParser.REGRESIONLOGISTICA) | (1 << UNaIAParser.BAYES) | (1 << UNaIAParser.KNN) | (1 << UNaIAParser.SVM) | (1 << UNaIAParser.ARBOLDEDESICION) | (1 << UNaIAParser.BOSQUEALEATORIO) | (1 << UNaIAParser.AUTO))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetodoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entrenamiento(self):
            return self.getTypedRuleContext(UNaIAParser.EntrenamientoContext,0)


        def evaluacion(self):
            return self.getTypedRuleContext(UNaIAParser.EvaluacionContext,0)


        def prediccion(self):
            return self.getTypedRuleContext(UNaIAParser.PrediccionContext,0)


        def reporte(self):
            return self.getTypedRuleContext(UNaIAParser.ReporteContext,0)


        def estadisticas(self):
            return self.getTypedRuleContext(UNaIAParser.EstadisticasContext,0)


        def graficas(self):
            return self.getTypedRuleContext(UNaIAParser.GraficasContext,0)


        def getRuleIndex(self):
            return UNaIAParser.RULE_metodo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetodo" ):
                listener.enterMetodo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetodo" ):
                listener.exitMetodo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetodo" ):
                return visitor.visitMetodo(self)
            else:
                return visitor.visitChildren(self)




    def metodo(self):

        localctx = UNaIAParser.MetodoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_metodo)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [UNaIAParser.ENTRENAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.entrenamiento()
                pass
            elif token in [UNaIAParser.EVALUAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.evaluacion()
                pass
            elif token in [UNaIAParser.PREDECIR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.prediccion()
                pass
            elif token in [UNaIAParser.REPORTAR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.reporte()
                pass
            elif token in [UNaIAParser.ESTADISTICAS]:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.estadisticas()
                pass
            elif token in [UNaIAParser.GRAFICAR]:
                self.enterOuterAlt(localctx, 6)
                self.state = 70
                self.graficas()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntrenamientoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTRENAR(self):
            return self.getToken(UNaIAParser.ENTRENAR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.ID)
            else:
                return self.getToken(UNaIAParser.ID, i)

        def CON(self):
            return self.getToken(UNaIAParser.CON, 0)

        def getRuleIndex(self):
            return UNaIAParser.RULE_entrenamiento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntrenamiento" ):
                listener.enterEntrenamiento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntrenamiento" ):
                listener.exitEntrenamiento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntrenamiento" ):
                return visitor.visitEntrenamiento(self)
            else:
                return visitor.visitChildren(self)




    def entrenamiento(self):

        localctx = UNaIAParser.EntrenamientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_entrenamiento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(UNaIAParser.ENTRENAR)
            self.state = 74
            self.match(UNaIAParser.ID)
            self.state = 75
            self.match(UNaIAParser.CON)
            self.state = 76
            self.match(UNaIAParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EvaluacionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EVALUAR(self):
            return self.getToken(UNaIAParser.EVALUAR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.ID)
            else:
                return self.getToken(UNaIAParser.ID, i)

        def CON(self):
            return self.getToken(UNaIAParser.CON, 0)

        def getRuleIndex(self):
            return UNaIAParser.RULE_evaluacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvaluacion" ):
                listener.enterEvaluacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvaluacion" ):
                listener.exitEvaluacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvaluacion" ):
                return visitor.visitEvaluacion(self)
            else:
                return visitor.visitChildren(self)




    def evaluacion(self):

        localctx = UNaIAParser.EvaluacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_evaluacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(UNaIAParser.EVALUAR)
            self.state = 79
            self.match(UNaIAParser.ID)
            self.state = 80
            self.match(UNaIAParser.CON)
            self.state = 81
            self.match(UNaIAParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrediccionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREDECIR(self):
            return self.getToken(UNaIAParser.PREDECIR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.ID)
            else:
                return self.getToken(UNaIAParser.ID, i)

        def CON(self):
            return self.getToken(UNaIAParser.CON, 0)

        def getRuleIndex(self):
            return UNaIAParser.RULE_prediccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrediccion" ):
                listener.enterPrediccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrediccion" ):
                listener.exitPrediccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrediccion" ):
                return visitor.visitPrediccion(self)
            else:
                return visitor.visitChildren(self)




    def prediccion(self):

        localctx = UNaIAParser.PrediccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_prediccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(UNaIAParser.PREDECIR)
            self.state = 84
            self.match(UNaIAParser.ID)
            self.state = 85
            self.match(UNaIAParser.CON)
            self.state = 86
            self.match(UNaIAParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReporteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPORTAR(self):
            return self.getToken(UNaIAParser.REPORTAR, 0)

        def ID(self):
            return self.getToken(UNaIAParser.ID, 0)

        def PAR_IZQ(self):
            return self.getToken(UNaIAParser.PAR_IZQ, 0)

        def PAR_DER(self):
            return self.getToken(UNaIAParser.PAR_DER, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.COMA)
            else:
                return self.getToken(UNaIAParser.COMA, i)

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.NUMERO)
            else:
                return self.getToken(UNaIAParser.NUMERO, i)

        def getRuleIndex(self):
            return UNaIAParser.RULE_reporte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReporte" ):
                listener.enterReporte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReporte" ):
                listener.exitReporte(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReporte" ):
                return visitor.visitReporte(self)
            else:
                return visitor.visitChildren(self)




    def reporte(self):

        localctx = UNaIAParser.ReporteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_reporte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(UNaIAParser.REPORTAR)
            self.state = 89
            self.match(UNaIAParser.ID)
            self.state = 90
            self.match(UNaIAParser.PAR_IZQ)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==UNaIAParser.COMA:
                self.state = 91
                self.match(UNaIAParser.COMA)
                self.state = 92
                self.match(UNaIAParser.NUMERO)
                self.state = 93
                self.match(UNaIAParser.COMA)
                self.state = 94
                self.match(UNaIAParser.NUMERO)


            self.state = 97
            self.match(UNaIAParser.PAR_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstadisticasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESTADISTICAS(self):
            return self.getToken(UNaIAParser.ESTADISTICAS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.ID)
            else:
                return self.getToken(UNaIAParser.ID, i)

        def CON(self):
            return self.getToken(UNaIAParser.CON, 0)

        def getRuleIndex(self):
            return UNaIAParser.RULE_estadisticas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstadisticas" ):
                listener.enterEstadisticas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstadisticas" ):
                listener.exitEstadisticas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEstadisticas" ):
                return visitor.visitEstadisticas(self)
            else:
                return visitor.visitChildren(self)




    def estadisticas(self):

        localctx = UNaIAParser.EstadisticasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_estadisticas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(UNaIAParser.ESTADISTICAS)
            self.state = 100
            self.match(UNaIAParser.ID)
            self.state = 101
            self.match(UNaIAParser.CON)
            self.state = 102
            self.match(UNaIAParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraficasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GRAFICAR(self):
            return self.getToken(UNaIAParser.GRAFICAR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.ID)
            else:
                return self.getToken(UNaIAParser.ID, i)

        def CON(self):
            return self.getToken(UNaIAParser.CON, 0)

        def getRuleIndex(self):
            return UNaIAParser.RULE_graficas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraficas" ):
                listener.enterGraficas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraficas" ):
                listener.exitGraficas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraficas" ):
                return visitor.visitGraficas(self)
            else:
                return visitor.visitChildren(self)




    def graficas(self):

        localctx = UNaIAParser.GraficasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_graficas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(UNaIAParser.GRAFICAR)
            self.state = 105
            self.match(UNaIAParser.ID)
            self.state = 106
            self.match(UNaIAParser.CON)
            self.state = 107
            self.match(UNaIAParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





