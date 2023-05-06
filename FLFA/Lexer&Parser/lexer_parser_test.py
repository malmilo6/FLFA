from lexer import Lexer
from parser1 import Parser
from ast import Identifier, Operator, Integer, String, VariableDeclaration


def main():

    with open('source_code.txt', 'r') as file:
        source_code = file.read()
    lex = Lexer(source_code)

    tokens = lex.tokenize()
    pars = Parser(tokens)
    ast_nodes = pars.parse()

    # Print the AST nodes
    for node in ast_nodes:
        print(node.__class__.__name__)
        if isinstance(node, VariableDeclaration):
            print("Identifier:", node.identifier.value)
            if isinstance(node.value, Integer):
                print("Value (Integer):", node.value.value)
            elif isinstance(node.value, String):
                print("Value (String):", node.value.value)


if "__name__" == main():
    main()
