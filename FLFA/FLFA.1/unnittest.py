import unittest
from converter import Converter


class TestConverter(unittest.TestCase):

    def test_remove_epsilon_productions(self):
        variables = {"S", "A", "B", "D", 'C'}
        terminals = {"a", "b"}
        productions = [("S", "a"), ("S", "aD"), ("D", "aD"), ("S", "aA"), ("S", "B"),
                       ("A", "aBB"), ("A", "ε"), ("B", "Aa"), ("B", "b"), ("C", "aC")]
        C = Converter(variables, terminals, productions)
        new_variables, new_terminals, new_productions = C.remove_epsilon_productions(C.variables, C.terminals,
                                                                                     C.productions)
        expected_productions = [('S', 'a'), ('S', 'aD'), ('D', 'aD'), ('S', 'aA'), ('S', 'B'), ('A', 'aBB'),
                                ('B', 'Aa'), ('B', 'a'), ('B', 'b'), ('C', 'aC')]
        self.assertCountEqual(new_productions, expected_productions)

    def test_remove_unit_productions(self):
        variables = {"S", "A", "B", "D", 'C'}
        terminals = {"a", "b"}
        productions = [('S', 'a'), ('S', 'aD'), ('D', 'aD'), ('S', 'aA'), ('S', 'B'), ('A', 'aBB'), ('B', 'Aa'),
                       ('B', 'a'), ('B', 'b'), ('C', 'aC')]
        C = Converter(variables, terminals, productions)
        new_variables, new_terminals, new_productions = C.remove_unit_productions(C.variables, C.terminals,
                                                                                  C.productions)
        expected_productions = [('S', 'aA'), ('C', 'aC'), ('B', 'a'), ('S', 'b'), ('D', 'aD'), ('S', 'a'), ('B', 'b'),
                                ('S', 'Aa'), ('A', 'aBB'), ('S', 'aD'), ('B', 'Aa')]
        self.assertCountEqual(new_productions, expected_productions)

    def test_inaccessible_symbols(self):
        variables = {"S", "A", "B", "D", 'C'}
        terminals = {"a", "b"}
        productions = [('S', 'aA'), ('C', 'aC'), ('B', 'a'), ('S', 'b'), ('D', 'aD'), ('S', 'a'), ('B', 'b'),
                       ('S', 'Aa'), ('A', 'aBB'), ('S', 'aD'), ('B', 'Aa')]
        C = Converter(variables, terminals, productions)
        new_variables, new_terminals, new_productions = C.remove_inaccessible_symbols(C.variables, C.terminals,
                                                                                      C.productions)
        expected_productions = [('S', 'aA'), ('B', 'a'), ('S', 'b'), ('D', 'aD'), ('S', 'a'), ('B', 'b'), ('S', 'Aa'),
                                ('A', 'aBB'), ('S', 'aD'), ('B', 'Aa')]
        expected_variables = {'S', 'A', 'B', 'D'}
        self.assertCountEqual(new_productions, expected_productions)
        self.assertCountEqual(new_variables, expected_variables)

    def test_remove_nonproductive_symbols(self):
        variables = {'S', 'A', 'B', 'D'}
        terminals = {'a', 'b'}
        productions = [('S', 'aA'), ('B', 'a'), ('S', 'b'), ('D', 'aD'), ('S', 'a'), ('B', 'b'), ('S', 'Aa'),
                       ('A', 'aBB'), ('S', 'aD'), ('B', 'Aa')]
        C = Converter(variables, terminals, productions)
        new_variables, new_terminals, new_productions = C.remove_nonproductive_symbols(C.variables, C.terminals,
                                                                                      C.productions)
        expected_productions = [('S', 'aA'), ('B', 'a'), ('S', 'b'), ('S', 'a'), ('B', 'b'), ('S', 'Aa'), ('A', 'aBB'), ('B', 'Aa')]
        expected_variables = {'A', 'B', 'S'}
        self.assertCountEqual(new_productions, expected_productions)
        self.assertCountEqual(new_variables, expected_variables)

    def test_to_cnf(self):
        variables = {'S', 'A', 'B'}
        terminals = {'a', 'b'}
        productions = [('S', 'aA'), ('S', 'b'), ('A', 'aBB'), ('S', 'a'), ('B', 'b'), ('S', 'Aa'), ('B', 'a'), ('B', 'Aa')]
        C = Converter(variables, terminals, productions)
        new_variables, new_terminals, new_productions = C.to_cnf(variables, terminals, productions)

        expected_productions = [('T1', 'a'), ('S', 'T1A'), ('T2', 'b'), ('S', 'T2'), ('A', 'aX3'), ('X3', 'BB'),
                                ('S', 'T1'), ('B', 'T2'), ('S', 'AT1'), ('B', 'T1'), ('B', 'AT1')]
        expected_variables = {'S', 'T1', 'T2', 'X3', 'A', 'B'}
        self.assertCountEqual(new_productions, expected_productions)
        self.assertCountEqual(new_variables, expected_variables)


if __name__ == '__unittest__':
    unittest.main()
