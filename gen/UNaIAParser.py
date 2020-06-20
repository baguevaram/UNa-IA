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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\7\2\27\n\2\f\2\16\2\32\13")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\5\3!\n\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3(\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\48\n\4\3\5\3\5\3\5\3\5\3\5\5\5?\n\5\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\7\5\7H\n\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\3\3\2\n\17")
        buf.write("\2_\2\30\3\2\2\2\4\'\3\2\2\2\6\67\3\2\2\2\b9\3\2\2\2\n")
        buf.write("B\3\2\2\2\fG\3\2\2\2\16I\3\2\2\2\20P\3\2\2\2\22W\3\2\2")
        buf.write("\2\24\27\5\6\4\2\25\27\5\f\7\2\26\24\3\2\2\2\26\25\3\2")
        buf.write("\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\3\3")
        buf.write("\2\2\2\32\30\3\2\2\2\33\34\7\4\2\2\34\35\7\23\2\2\35 ")
        buf.write("\7\26\2\2\36\37\7\20\2\2\37!\7\26\2\2 \36\3\2\2\2 !\3")
        buf.write("\2\2\2!\"\3\2\2\2\"(\7\24\2\2#$\7\5\2\2$%\7\23\2\2%&\7")
        buf.write("\26\2\2&(\7\24\2\2\'\33\3\2\2\2\'#\3\2\2\2(\5\3\2\2\2")
        buf.write(")*\7\25\2\2*+\7\22\2\2+8\5\4\3\2,-\7\25\2\2-.\7\22\2\2")
        buf.write(".8\5\n\6\2/\60\7\25\2\2\60\61\7\22\2\2\618\5\f\7\2\62")
        buf.write("\63\7\25\2\2\63\64\7\20\2\2\64\65\7\25\2\2\65\66\7\22")
        buf.write("\2\2\668\5\b\5\2\67)\3\2\2\2\67,\3\2\2\2\67/\3\2\2\2\67")
        buf.write("\62\3\2\2\28\7\3\2\2\29:\7\t\2\2:;\7\23\2\2;>\7\25\2\2")
        buf.write("<=\7\20\2\2=?\7\27\2\2><\3\2\2\2>?\3\2\2\2?@\3\2\2\2@")
        buf.write("A\7\24\2\2A\t\3\2\2\2BC\t\2\2\2C\13\3\2\2\2DH\5\16\b\2")
        buf.write("EH\5\20\t\2FH\5\22\n\2GD\3\2\2\2GE\3\2\2\2GF\3\2\2\2H")
        buf.write("\r\3\2\2\2IJ\7\25\2\2JK\7\21\2\2KL\7\6\2\2LM\7\23\2\2")
        buf.write("MN\7\25\2\2NO\7\24\2\2O\17\3\2\2\2PQ\7\25\2\2QR\7\21\2")
        buf.write("\2RS\7\7\2\2ST\7\23\2\2TU\7\25\2\2UV\7\24\2\2V\21\3\2")
        buf.write("\2\2WX\7\25\2\2XY\7\21\2\2YZ\7\b\2\2Z[\7\23\2\2[\\\7\25")
        buf.write("\2\2\\]\7\24\2\2]\23\3\2\2\2\t\26\30 \'\67>G")
        return buf.getvalue()


class UNaIAParser ( Parser ):

    grammarFileName = "UNaIA.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'ejemplos'", "'datos'", 
                     "'entrenar'", "'evaluar'", "'predecir'", "'dividirDatos'", 
                     "'regresionLogistica'", "'bayes'", "'knn'", "'svm'", 
                     "'arbolDeDecision'", "'bosqueAleatorio'", "','", "'.'", 
                     "'='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "EJEMPLOS", "DATOS", "ENTRENAR", 
                      "EVALUAR", "PREDECIR", "DIVIDIRDATOS", "REGRESIONLOGISTICA", 
                      "BAYES", "KNN", "SVM", "ARBOLDEDESICION", "BOSQUEALEATORIO", 
                      "COMA", "PUNTO", "ASIG", "PAR_IZQ", "PAR_DER", "ID", 
                      "STRING", "NUMERO", "ESPACIO" ]

    RULE_programa = 0
    RULE_datos = 1
    RULE_asignacion = 2
    RULE_division = 3
    RULE_modelo = 4
    RULE_metodo = 5
    RULE_entrenamiento = 6
    RULE_evaluacion = 7
    RULE_prediccion = 8

    ruleNames =  [ "programa", "datos", "asignacion", "division", "modelo", 
                   "metodo", "entrenamiento", "evaluacion", "prediccion" ]

    EOF = Token.EOF
    COMMENT=1
    EJEMPLOS=2
    DATOS=3
    ENTRENAR=4
    EVALUAR=5
    PREDECIR=6
    DIVIDIRDATOS=7
    REGRESIONLOGISTICA=8
    BAYES=9
    KNN=10
    SVM=11
    ARBOLDEDESICION=12
    BOSQUEALEATORIO=13
    COMA=14
    PUNTO=15
    ASIG=16
    PAR_IZQ=17
    PAR_DER=18
    ID=19
    STRING=20
    NUMERO=21
    ESPACIO=22

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
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==UNaIAParser.ID:
                self.state = 20
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 18
                    self.asignacion()
                    pass

                elif la_ == 2:
                    self.state = 19
                    self.metodo()
                    pass


                self.state = 24
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
        def PAR_IZQ(self):
            return self.getToken(UNaIAParser.PAR_IZQ, 0)
        def STRING(self):
            return self.getToken(UNaIAParser.STRING, 0)
        def PAR_DER(self):
            return self.getToken(UNaIAParser.PAR_DER, 0)

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
        def PAR_IZQ(self):
            return self.getToken(UNaIAParser.PAR_IZQ, 0)
        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.STRING)
            else:
                return self.getToken(UNaIAParser.STRING, i)
        def PAR_DER(self):
            return self.getToken(UNaIAParser.PAR_DER, 0)
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
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [UNaIAParser.EJEMPLOS]:
                localctx = UNaIAParser.DatosEjemplosContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(UNaIAParser.EJEMPLOS)
                self.state = 26
                self.match(UNaIAParser.PAR_IZQ)
                self.state = 27
                self.match(UNaIAParser.STRING)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==UNaIAParser.COMA:
                    self.state = 28
                    self.match(UNaIAParser.COMA)
                    self.state = 29
                    self.match(UNaIAParser.STRING)


                self.state = 32
                self.match(UNaIAParser.PAR_DER)
                pass
            elif token in [UNaIAParser.DATOS]:
                localctx = UNaIAParser.DatosDatosContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(UNaIAParser.DATOS)
                self.state = 34
                self.match(UNaIAParser.PAR_IZQ)
                self.state = 35
                self.match(UNaIAParser.STRING)
                self.state = 36
                self.match(UNaIAParser.PAR_DER)
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
        def COMA(self):
            return self.getToken(UNaIAParser.COMA, 0)
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
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = UNaIAParser.AsigDatosContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(UNaIAParser.ID)
                self.state = 40
                self.match(UNaIAParser.ASIG)
                self.state = 41
                self.datos()
                pass

            elif la_ == 2:
                localctx = UNaIAParser.AsigModeloContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(UNaIAParser.ID)
                self.state = 43
                self.match(UNaIAParser.ASIG)
                self.state = 44
                self.modelo()
                pass

            elif la_ == 3:
                localctx = UNaIAParser.AsigMetodoContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(UNaIAParser.ID)
                self.state = 46
                self.match(UNaIAParser.ASIG)
                self.state = 47
                self.metodo()
                pass

            elif la_ == 4:
                localctx = UNaIAParser.AsigMultiContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.match(UNaIAParser.ID)
                self.state = 49
                self.match(UNaIAParser.COMA)
                self.state = 50
                self.match(UNaIAParser.ID)
                self.state = 51
                self.match(UNaIAParser.ASIG)
                self.state = 52
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

        def PAR_IZQ(self):
            return self.getToken(UNaIAParser.PAR_IZQ, 0)

        def ID(self):
            return self.getToken(UNaIAParser.ID, 0)

        def PAR_DER(self):
            return self.getToken(UNaIAParser.PAR_DER, 0)

        def COMA(self):
            return self.getToken(UNaIAParser.COMA, 0)

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
            self.state = 55
            self.match(UNaIAParser.DIVIDIRDATOS)
            self.state = 56
            self.match(UNaIAParser.PAR_IZQ)
            self.state = 57
            self.match(UNaIAParser.ID)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==UNaIAParser.COMA:
                self.state = 58
                self.match(UNaIAParser.COMA)
                self.state = 59
                self.match(UNaIAParser.NUMERO)


            self.state = 62
            self.match(UNaIAParser.PAR_DER)
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
            self.state = 64
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << UNaIAParser.REGRESIONLOGISTICA) | (1 << UNaIAParser.BAYES) | (1 << UNaIAParser.KNN) | (1 << UNaIAParser.SVM) | (1 << UNaIAParser.ARBOLDEDESICION) | (1 << UNaIAParser.BOSQUEALEATORIO))) != 0)):
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
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.entrenamiento()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.evaluacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.prediccion()
                pass


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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.ID)
            else:
                return self.getToken(UNaIAParser.ID, i)

        def PUNTO(self):
            return self.getToken(UNaIAParser.PUNTO, 0)

        def ENTRENAR(self):
            return self.getToken(UNaIAParser.ENTRENAR, 0)

        def PAR_IZQ(self):
            return self.getToken(UNaIAParser.PAR_IZQ, 0)

        def PAR_DER(self):
            return self.getToken(UNaIAParser.PAR_DER, 0)

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
            self.state = 71
            self.match(UNaIAParser.ID)
            self.state = 72
            self.match(UNaIAParser.PUNTO)
            self.state = 73
            self.match(UNaIAParser.ENTRENAR)
            self.state = 74
            self.match(UNaIAParser.PAR_IZQ)
            self.state = 75
            self.match(UNaIAParser.ID)
            self.state = 76
            self.match(UNaIAParser.PAR_DER)
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.ID)
            else:
                return self.getToken(UNaIAParser.ID, i)

        def PUNTO(self):
            return self.getToken(UNaIAParser.PUNTO, 0)

        def EVALUAR(self):
            return self.getToken(UNaIAParser.EVALUAR, 0)

        def PAR_IZQ(self):
            return self.getToken(UNaIAParser.PAR_IZQ, 0)

        def PAR_DER(self):
            return self.getToken(UNaIAParser.PAR_DER, 0)

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
            self.match(UNaIAParser.ID)
            self.state = 79
            self.match(UNaIAParser.PUNTO)
            self.state = 80
            self.match(UNaIAParser.EVALUAR)
            self.state = 81
            self.match(UNaIAParser.PAR_IZQ)
            self.state = 82
            self.match(UNaIAParser.ID)
            self.state = 83
            self.match(UNaIAParser.PAR_DER)
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.ID)
            else:
                return self.getToken(UNaIAParser.ID, i)

        def PUNTO(self):
            return self.getToken(UNaIAParser.PUNTO, 0)

        def PREDECIR(self):
            return self.getToken(UNaIAParser.PREDECIR, 0)

        def PAR_IZQ(self):
            return self.getToken(UNaIAParser.PAR_IZQ, 0)

        def PAR_DER(self):
            return self.getToken(UNaIAParser.PAR_DER, 0)

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
            self.state = 85
            self.match(UNaIAParser.ID)
            self.state = 86
            self.match(UNaIAParser.PUNTO)
            self.state = 87
            self.match(UNaIAParser.PREDECIR)
            self.state = 88
            self.match(UNaIAParser.PAR_IZQ)
            self.state = 89
            self.match(UNaIAParser.ID)
            self.state = 90
            self.match(UNaIAParser.PAR_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





