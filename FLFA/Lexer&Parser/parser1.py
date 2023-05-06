from ast import Identifier, Operator, Integer, String, VariableDeclaration


class Parser(object):

    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0

    def parse(self):
        ast_nodes = []

        while self.token_index < len(self.tokens):
            token_type = self.tokens[self.token_index][0]
            token_value = self.tokens[self.token_index][1]

            if token_type == 'DECLARATION' and token_value == 'var':
                var_decl_node = self.parse_var_declaration(
                    self.tokens[self.token_index:len(self.tokens)])
                ast_nodes.append(var_decl_node)

            self.token_index += 1

        return ast_nodes

    def parse_var_declaration(self, tokens):
        tokens_verified = 0
        identifier = None
        operator = None
        value = None

        for token in range(0, len(tokens)):

            token_type = tokens[tokens_verified][0]
            token_value = tokens[tokens_verified][1]

            if token == 0:
                pass  # Ignore variable type, since it's not needed in the AST

            elif token == 1 and token_type == 'IDENTIFIER':
                identifier = Identifier(token_value)
            elif token == 1 and token_type != 'IDENTIFIER':
                raise ValueError('Error: Invalid variable name: ' + token_value)

            elif token == 2 and token_type == 'OPERATOR':
                operator = Operator(token_value)
            elif token == 2 and token_type != 'OPERATOR':
                raise ValueError('Error: Invalid assign operator ')

            elif token == 3 and token_type in ['IDENTIFIER', 'INTEGER', 'STRING']:
                if token_type == 'INTEGER':
                    value = Integer(token_value)
                elif token_type == 'IDENTIFIER':
                    value = Identifier(token_value)
                elif token_type == 'STRING':
                    value = String(token_value)

            elif token == 4 and token_type == 'SEPARATOR':
                pass  # Ignore the separator, since it's not needed in the AST

            tokens_verified += 1

        variable_declaration = VariableDeclaration(identifier, value)
        self.token_index += tokens_verified

        return variable_declaration