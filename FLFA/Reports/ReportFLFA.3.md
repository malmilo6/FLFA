# Topic: Lexer
## Course: Formal Languages & Finite Automata
### Author: Cernetchi Maxim
## Theory 
<p>
Lexical analysis, also known as tokenization, is the process of analyzing and breaking down a sequence of characters (source code) into a series of meaningful tokens (lexical units). This is the first step in the compilation process of computer programs, where the source code is translated into machine-readable code.

The purpose of lexical analysis is to recognize and group characters into tokens that represent the basic units of the programming language. These tokens are later processed by the compiler or interpreter to generate executable code.

The lexical analysis process involves the use of a lexical analyzer, also known as a lexer or scanner, which scans the source code character by character and groups them into tokens based on predefined rules or regular expressions. For example, in the C programming language, a keyword such as "if" or "while" is recognized as a token, as well as variable names, numeric constants, and operators.

Lexical analysis plays a critical role in the compilation process, as it ensures that the source code is correctly translated into machine-readable code. It also helps in error detection, as the lexer can identify and report lexical errors, such as unrecognized characters or invalid tokens.
</p>

### How does the Lexer work?
The lexer generates a stream of tokens, which are passed on to the parser for further processing. The parser analyzes the structure of the program based on the grammar of the programming language and generates a parse tree, which represents the structure of the program.

## Objectives:
1. Understand what lexical analysis is.
2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
3. Implement a sample lexer and show how it works.

## Implementation description
This implementation is a simple lexer, written in Python, that tokenizes a given source code. It uses regular expressions to recognize different types of tokens such as variable declaration, integers, identifiers, operators, and separators.

The Lexer class is initialized with the source code, which is then tokenized by the tokenize() method. The method first splits the source code into a list of "tokens" using whitespace as a delimiter. It then iterates over each token and checks its type by using regular expressions and conditional statements.
```    
        def tokenize(self):
        # This list will keep all tokens
        tokens = []

        # Splitting the source code into "tokens"
        source_code = self.source_code.split()
```
If the token is "var", it is recognized as a variable declaration and added to the list of tokens. If the token is a digit, it is recognized as an integer, and if it ends with a semicolon, it is added to the list of tokens as an INTEGER token with the semicolon removed. If the token is a word, it is recognized as an identifier and added to the list of tokens. If it ends with a semicolon, it is added to the list of tokens as an IDENTIFIER token with the semicolon removed. If the token is one of the supported operators (+, -, =, *, /), it is recognized as an operator and added to the list of tokens. If the token ends with a semicolon, it is recognized as a separator and added to the list of tokens.
``` 
            if token == "var":
                tokens.append(['DECLARATION', token])

            # Recognise an integer
            elif re.match('[0-9]', token):
                if token[-1] == ";":
                    tokens.append(['INTEGER', token[:-1]])
                else:
                    tokens.append(['INTEGER', token])

            # Recognise a word
            elif re.match('[a-z]', token) or re.match('[A-Z]', token):
                if token[-1] == ";":
                    tokens.append(['IDENTIFIER', token[:-1]])
                else:
                    tokens.append(['IDENTIFIER', token])

            # Recognise an operation
            elif token in "+-=/*":
                tokens.append(['OPERATOR', token])

            # Recognise the separator, for this case also end of declaration
            if token[-1] == ";":
                tokens.append(['SEPARATOR', token[-1]])
 ```
The resulting list of tokens is returned by the tokenize() method. Each token is represented as a list with two elements: the type of the token and its value. For example, a variable declaration token would be represented as ['DECLARATION', 'var'].

It's important to note that this implementation can only handle a limited set of tokens from given simple source code and source code patterns. In practice, a lexer would need to be much more sophisticated and able to handle a wider range of input.

## Conclusion
In conclusion, lexical analysis is an important step in the compilation process of programming languages. It involves breaking down a sequence of characters in the source code into meaningful tokens, which can then be processed further to generate executable code. The implementation of a lexer, such as the one provided, can be useful for understanding the basic principles of lexical analysis.

The given code is a simple lexer written in Python, which tokenizes the source code by using regular expressions and conditional statements. It recognizes different types of tokens such as variable declarations, integers, identifiers, operators, and separators. However, it is important to note that this implementation is limited in its ability to handle a wide range of input and is not robust enough for practical use.

Overall, this implementation provides a useful starting point for understanding the basics of lexical analysis and can be built upon to create more sophisticated lexers for handling real-world programming languages.
