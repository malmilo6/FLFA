class Parser(object):

    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0

    def parse(self):
        while self.token_index < len(self.tokens):
            token_type = self.tokens[self.token_index][0]
            token_value = self.tokens[self.token_index][1]

            # Trigger var declaration
            if token_type == 'DECLARATION' and token_value == 'var':
                self.parse_var_declaration(self.tokens[self.token_index:len(self.tokens)])
            # Increment token index
            self.token_index += 1

    def parse_var_declaration(self, tokens):

        tokens_verified = 0

        for token in range(0, len(tokens)):

            token_type = tokens[tokens_verified][0]
            token_value = tokens[tokens_verified][1]

            # Get var type
            if token == 0:
                print('Variable type: ' + token_value)

            # Get variable name
            elif token == 1 and token_type == 'IDENTIFIER':
                print('Var name: ' + token_value)
            elif token == 1 and token_type != 'IDENTIFIER':
                print('Error: Invalid variable name: ' + token_value)
                quit()

            # Get assignment operator
            elif token == 2 and token_type == 'OPERATOR':
                print('Assign operator: ' + token_value)
            elif token == 2 and token_type != 'OPERATOR':
                print('Error: Invalid assign operator ')
                quit()

            # Get variable value
            elif token == 3 and token_type in ['IDENTIFIER', 'INTEGER', 'STRING']:
                print('Var value: ' + token_value)
            elif token == 3 and token_type not in ['IDENTIFIER', 'INTEGER', 'STRING']:
                print('Invalid var assign value' + token_value)
                quit()

            # Get end of statement
            elif token == 4 and token_type == 'SEPARATOR':
                print('End of declaration: ' + token_value)
            elif token == 4 and token_type != 'SEPARATOR':
                print("Error: End of declaration statement expected ';'")
                quit()

            tokens_verified += 1
