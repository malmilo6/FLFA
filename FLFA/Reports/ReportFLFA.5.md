# Topic: Parser & Building an Abstract Syntax Tree

### Course: Formal Languages & Finite Automata
### Author: Cernetchi Maxim
## Theory
#### Parsing
Parsing, also known as syntax analysis or syntactic analysis, is the process of analyzing a sequence of tokens, usually generated from a lexer, to determine their grammatical structure with respect to a given formal grammar. In other words, parsing is the process of converting a linear representation of a program (source code) into a hierarchical structure, often in the form of an Abstract Syntax Tree (AST), that more accurately represents the program's structure according to the programming language's syntax rules.

The main purpose of parsing is to ensure that the input program conforms to the syntactical rules of the programming language and to detect and report syntax errors if any. It is an essential step in the process of compiling, interpreting, or analyzing programming languages, as it allows the subsequent stages, such as semantic analysis, code optimization, or code generation, to work with a well-defined, hierarchical structure.

There are two primary approaches to parsing:

1. Top-down parsing: This method starts with the root of the parse tree (usually the starting symbol of the grammar) and attempts to derive the input tokens by applying the grammar rules in a top-down manner. Recursive Descent and LL parsers are examples of top-down parsers.

2. Bottom-up parsing: This method starts with the input tokens and tries to construct the parse tree by applying grammar rules in a bottom-up manner. The idea is to reduce the input tokens to the root symbol of the grammar by iteratively applying the rules in reverse. LR parsers (including SLR, LALR, and Canonical LR) and the Shift-Reduce parser are examples of bottom-up parsers.

Each approach has its advantages and disadvantages in terms of performance, complexity, and ease of implementation. Choosing the appropriate parsing method depends on the specific language being parsed and the requirements of the application.
#### AST
An Abstract Syntax Tree (AST) is a tree-based representation of the structure of a program's source code. It is an intermediate data structure created during the parsing phase of a compiler or interpreter, following the syntax analysis. The AST abstracts away the syntactic details of the source code, such as parentheses or semicolons, and focuses on the hierarchical organization of the code.

Each node in the AST represents a programming construct, such as a function, a variable declaration, an assignment, a loop, a conditional statement, or an expression. The edges between the nodes represent the relationships between these constructs. The AST can be thought of as a high-level representation of the program's logic, which is more easily processed and manipulated by the subsequent stages of a compiler or interpreter.

The main advantages of using an AST include:

1. Easier processing: The hierarchical structure of the AST simplifies the processing of the source code during later stages, such as semantic analysis, code optimization, or code generation.

2. Language-agnostic representation: An AST can be generated for any programming language, making it a flexible and reusable representation for different language processors.

3. Simplified code transformation: The AST enables simple and efficient manipulation of the code structure, such as code optimizations, transformations, or refactoring.

4. Improved error reporting: With an AST, it is easier to detect and report syntax and semantic errors, as well as to provide meaningful error messages, as the hierarchical structure provides context to the code constructs.
## Objectives:
1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST [2].
3. In addition to what has been done in the 3rd lab work do the following:
   1. In case you didn't have a type that denotes the possible types of tokens you need to:
      1. Have a type __*TokenType*__ (like an enum) that can be used in the lexical analysis to categorize the tokens. 
      2. Please use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.

## Implementation description
1. **Abstract Syntax Tree (AST) Node Classes:**
The implementation starts by defining a base Node class and several subclasses representing different types of nodes in the AST. Each subclass has an **___init___** method for initializing the node with the required attributes.
```
class Node:
    pass

class VariableDeclaration(Node):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

# Other node classes: Assignment, Identifier, Integer, String, Operator
```
2. **Parser Class:**
A Parser class is defined that takes a list of tokens generated by a lexer and converts them into a list of AST nodes. The class provides functions for parsing variable declarations **_parse_var_declaration_** and building the AST **_parse_**.
```
class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0

    def parse(self):
        ast_nodes = []
        # Parse the tokens and build the AST nodes

    def parse_var_declaration(self, tokens):
        # Parse a variable declaration and create an AST node for it

```

3. **Parsing Variable Declarations:**
The **_parse_var_declaration_** function iterates through the tokens in a variable declaration, creating the necessary _Identifier_, _Operator_, and _Value_ nodes (either _Integer_ or _String_). It then constructs a _VariableDeclaration_ node using these nodes.
```
def parse_var_declaration(self, tokens):
    tokens_verified = 0
    identifier = None
    operator = None
    value = None

    for token in range(0, len(tokens)):
        token_type = tokens[tokens_verified][0]
        token_value = tokens[tokens_verified][1]

        if token == 1 and token_type == 'IDENTIFIER':
            identifier = Identifier(token_value)
        elif token == 2 and token_type == 'OPERATOR':
            operator = Operator(token_value)
        elif token == 3 and token_type in ['IDENTIFIER', 'INTEGER', 'STRING']:
            # Create a Value node based on the token_type

    variable_declaration = VariableDeclaration(identifier, value)
    return variable_declaration

```

4. **_Building the AST:_**
The main parse function iterates through the tokens and calls **_parse_var_declaration_** whenever it encounters a variable declaration token. It then adds the returned _VariableDeclaration_ node to the ast_nodes list.
```
def parse(self):
    ast_nodes = []

    while self.token_index < len(self.tokens):
        token_type = self.tokens[self.token_index][0]
        token_value = self.tokens[self.token_index][1]

        if token_type == 'DECLARATION' and token_value == 'var':
            var_decl_node = self.parse_var_declaration(self.tokens[self.token_index:len(self.tokens)])
            ast_nodes.append(var_decl_node)

        self.token_index += 1

    return ast_nodes
```
## Results
For the provided source code, the AST will be the following one:

```var number = 15;```

```
VariableDeclaration
Identifier: number
Value (Integer): 15
```
## Conclusion
In summary, parsing, or syntactic analysis, is a fundamental step in the process of processing programming languages. It checks the conformity of the input program to the syntax rules of the language, creates a hierarchical structure (usually an AST), and allows for further processing in the compiler or interpreter pipeline. 
Abstract Syntax Tree (AST) is a tree-based representation of the structure of a program's source code that abstracts away the syntactic details and focuses on the hierarchical organization of the code. It is an essential component in the pipeline of compilers and interpreters, making the processing and manipulation of the source code easier and more efficient during the later stages.