from lexer import Lexer
from parser1 import Parser


def main():

    with open('source_code.txt', 'r') as file:
        source_code = file.read()
    lex = Lexer(source_code)

    tokens = lex.tokenize()
    print(lex.tokenize())

    pars = Parser(tokens)
    objects = pars.parse()


if "__name__" == main():
    main()
