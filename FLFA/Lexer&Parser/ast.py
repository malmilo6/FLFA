class Node:
    pass


class VariableDeclaration(Node):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value


class Assignment(Node):
    def __init__(self, identifier, operator, value):
        self.identifier = identifier
        self.operator = operator
        self.value = value


class Identifier(Node):
    def __init__(self, value):
        self.value = value


class Integer(Node):
    def __init__(self, value):
        self.value = value


class String(Node):
    def __init__(self, value):
        self.value = value


class Operator(Node):
    def __init__(self, value):
        self.value = value
