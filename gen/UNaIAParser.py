# Generated from /home/brayan/Documentos/UNAL/Semestre 9/Lenguajes/UNaIA/UNa-IA/Grammar/UNaIA.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\33\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\7\2\f\n\2\f\2")
        buf.write("\16\2\17\13\2\3\3\3\3\3\3\7\3\24\n\3\f\3\16\3\27\13\3")
        buf.write("\3\4\3\4\3\4\2\2\5\2\4\6\2\4\3\2\3\4\3\2\5\6\2\31\2\b")
        buf.write("\3\2\2\2\4\20\3\2\2\2\6\30\3\2\2\2\b\r\5\4\3\2\t\n\t\2")
        buf.write("\2\2\n\f\5\4\3\2\13\t\3\2\2\2\f\17\3\2\2\2\r\13\3\2\2")
        buf.write("\2\r\16\3\2\2\2\16\3\3\2\2\2\17\r\3\2\2\2\20\25\5\6\4")
        buf.write("\2\21\22\t\3\2\2\22\24\5\6\4\2\23\21\3\2\2\2\24\27\3\2")
        buf.write("\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\5\3\2\2\2\27\25\3")
        buf.write("\2\2\2\30\31\7\7\2\2\31\7\3\2\2\2\4\r\25")
        return buf.getvalue()


class UNaIAParser ( Parser ):

    grammarFileName = "UNaIA.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "MAS", "MENOS", "MULT", "DIV", "ENTERO", 
                      "ESPACIO" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_factor = 2

    ruleNames =  [ "expr", "term", "factor" ]

    EOF = Token.EOF
    MAS=1
    MENOS=2
    MULT=3
    DIV=4
    ENTERO=5
    ESPACIO=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UNaIAParser.TermContext)
            else:
                return self.getTypedRuleContext(UNaIAParser.TermContext,i)


        def MAS(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.MAS)
            else:
                return self.getToken(UNaIAParser.MAS, i)

        def MENOS(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.MENOS)
            else:
                return self.getToken(UNaIAParser.MENOS, i)

        def getRuleIndex(self):
            return UNaIAParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = UNaIAParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.term()
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==UNaIAParser.MAS or _la==UNaIAParser.MENOS:
                self.state = 7
                _la = self._input.LA(1)
                if not(_la==UNaIAParser.MAS or _la==UNaIAParser.MENOS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 8
                self.term()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(UNaIAParser.FactorContext)
            else:
                return self.getTypedRuleContext(UNaIAParser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.MULT)
            else:
                return self.getToken(UNaIAParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(UNaIAParser.DIV)
            else:
                return self.getToken(UNaIAParser.DIV, i)

        def getRuleIndex(self):
            return UNaIAParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = UNaIAParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.factor()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==UNaIAParser.MULT or _la==UNaIAParser.DIV:
                self.state = 15
                _la = self._input.LA(1)
                if not(_la==UNaIAParser.MULT or _la==UNaIAParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 16
                self.factor()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(UNaIAParser.ENTERO, 0)

        def getRuleIndex(self):
            return UNaIAParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = UNaIAParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(UNaIAParser.ENTERO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





