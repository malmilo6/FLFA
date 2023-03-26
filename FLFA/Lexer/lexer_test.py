import lexer


def main():
    source_code = ""

    with open('source_code.txt', 'r') as file:
        source_code = file.read()
    lex = lexer.Lexer(source_code)
    print(lex.tokenize())


if "__name__" == main():
    main()
