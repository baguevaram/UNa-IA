import warnings
warnings.filterwarnings("ignore")
from antlr4 import *
from UNaIALexer import UNaIALexer
from UNaIAParser import UNaIAParser
from src.MyVisitor import MyVisitor

def main():
    lexer = UNaIALexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = UNaIAParser(stream)
    tree = parser.programa()      #Regla inicial de la gramatica

    #print(tree.toStringTree(lexer,parser))

    loader = MyVisitor()
    loader.visit(tree)

if __name__ == '__main__':
    main()