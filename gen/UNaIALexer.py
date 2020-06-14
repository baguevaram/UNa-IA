# Generated from /home/brayan/Documentos/UNAL/Semestre 9/Lenguajes/UNaIA/UNa-IA/Grammar/UNaIA.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("#\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\6\6\31\n\6\r\6\16")
        buf.write("\6\32\3\7\6\7\36\n\7\r\7\16\7\37\3\7\3\7\2\2\b\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\3\2\3\5\2\13\f\17\17\"\"\2$\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\3\17\3\2\2\2\5\21\3\2\2\2\7\23\3\2\2\2\t")
        buf.write("\25\3\2\2\2\13\30\3\2\2\2\r\35\3\2\2\2\17\20\7-\2\2\20")
        buf.write("\4\3\2\2\2\21\22\7/\2\2\22\6\3\2\2\2\23\24\7,\2\2\24\b")
        buf.write("\3\2\2\2\25\26\7\61\2\2\26\n\3\2\2\2\27\31\4\62;\2\30")
        buf.write("\27\3\2\2\2\31\32\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2")
        buf.write("\33\f\3\2\2\2\34\36\t\2\2\2\35\34\3\2\2\2\36\37\3\2\2")
        buf.write("\2\37\35\3\2\2\2\37 \3\2\2\2 !\3\2\2\2!\"\b\7\2\2\"\16")
        buf.write("\3\2\2\2\5\2\32\37\3\2\3\2")
        return buf.getvalue()


class UNaIALexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MAS = 1
    MENOS = 2
    MULT = 3
    DIV = 4
    ENTERO = 5
    ESPACIO = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "MAS", "MENOS", "MULT", "DIV", "ENTERO", "ESPACIO" ]

    ruleNames = [ "MAS", "MENOS", "MULT", "DIV", "ENTERO", "ESPACIO" ]

    grammarFileName = "UNaIA.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


