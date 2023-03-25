class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
        tokens = []
        s_c = self.source_code.split()
        word_index = 0
        while word_index < len(s_c):
            tokens.append(s_c[word_index])
            word_index += 1
        return tokens
