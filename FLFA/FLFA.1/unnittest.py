import unittest
from converter import Converter


class TestConverter(unittest.TestCase):

    def test_remove_epsilon_productions(self):
        # Set up test data
        variables = {"S", "A", "B", "D", 'C'}
        terminals = {"a", "b"}
        productions = [("S", "a"), ("S", "aD"), ("D", "aD"), ("S", "aA"), ("S", "B"),
                       ("A", "aBB"), ("A", "ε"), ("B", "Aa"), ("B", "b"), ("C", "aC")]
        C = Converter(variables, terminals, productions)

        # Call remove_epsilon_productions
        new_variables, new_terminals, new_productions = C.remove_epsilon_productions(C.variables, C.terminals,
                                                                                     C.productions)
        # Define expected result
        expected_productions = [('S', 'a'), ('S', 'aD'), ('D', 'aD'), ('S', 'aA'), ('S', 'B'), ('A', 'aBB'),
                                ('B', 'Aa'), ('B', 'a'), ('B', 'b'), ('C', 'aC')]

        # Check if the new productions are equal to the expected result
        self.assertCountEqual(new_productions, expected_productions)

    def test_remove_unit_productions(self):
        # Set up test data
        variables = {"S", "A", "B", "D", 'C'}
        terminals = {"a", "b"}
        productions = [('S', 'a'), ('S', 'aD'), ('D', 'aD'), ('S', 'aA'), ('S', 'B'), ('A', 'aBB'), ('B', 'Aa'),
                       ('B', 'a'), ('B', 'b'), ('C', 'aC')]
        C = Converter(variables, terminals, productions)

        # Call remove_unit_productions
        new_variables, new_terminals, new_productions = C.remove_unit_productions(C.variables, C.terminals,
                                                                                  C.productions)
        # Define expected result
        expected_productions = [('S', 'aA'), ('C', 'aC'), ('B', 'a'), ('S', 'b'), ('D', 'aD'), ('S', 'a'), ('B', 'b'),
                                ('S', 'Aa'), ('A', 'aBB'), ('S', 'aD'), ('B', 'Aa')]

        # Check if the new productions are equal to the expected result
        self.assertCountEqual(new_productions, expected_productions)

    def test_inaccessible_symbols(self):
        # Set up test data
        variables = {"S", "A", "B", "D", 'C'}
        terminals = {"a", "b"}
        productions = [('S', 'aA'), ('C', 'aC'), ('B', 'a'), ('S', 'b'), ('D', 'aD'), ('S', 'a'), ('B', 'b'),
                       ('S', 'Aa'), ('A', 'aBB'), ('S', 'aD'), ('B', 'Aa')]
        C = Converter(variables, terminals, productions)

        # Call remove_inaccessible_symbols
        new_variables, new_terminals, new_productions = C.remove_inaccessible_symbols(C.variables, C.terminals,
                                                                                      C.productions)
        # Define expected result
        expected_productions = [('S', 'aA'), ('B', 'a'), ('S', 'b'), ('D', 'aD'), ('S', 'a'), ('B', 'b'), ('S', 'Aa'),
                                ('A', 'aBB'), ('S', 'aD'), ('B', 'Aa')]
        expected_variables = {'S', 'A', 'B', 'D'}

        # Check if the new productions and variables are equal to the expected result
        self.assertCountEqual(new_productions, expected_productions)
        self.assertCountEqual(new_variables, expected_variables)

    def test_remove_nonproductive_symbols(self):
        # Set up test data
        variables = {'S', 'A', 'B', 'D'}
        terminals = {'a', 'b'}
        productions = [('S', 'aA'), ('B', 'a'), ('S', 'b'), ('D', 'aD'), ('S', 'a'), ('B', 'b'), ('S', 'Aa'),
                       ('A', 'aBB'), ('S', 'aD'), ('B', 'Aa')]
        C = Converter(variables, terminals, productions)

        # Call remove_nonproductive_symbols
        new_variables, new_terminals, new_productions = C.remove_nonproductive_symbols(C.variables, C.terminals,
                                                                                       C.productions)
        # Define expected result
        expected_productions = [('S', 'aA'), ('B', 'a'), ('S', 'b'), ('S', 'a'), ('B', 'b'), ('S', 'Aa'), ('A', 'aBB'),
                                ('B', 'Aa')]
        expected_variables = {'A', 'B', 'S'}

        # Check if the new productions and variables are equal to the expected result
        self.assertCountEqual(new_productions, expected_productions)
        self.assertCountEqual(new_variables, expected_variables)

    def test_to_cnf(self):
        # Set up test data
        variables = {'S', 'A', 'B'}
        terminals = {'a', 'b'}
        productions = [('S', 'aA'), ('S', 'b'), ('A', 'aBB'), ('S', 'a'), ('B', 'b'), ('S', 'Aa'), ('B', 'a'),
                       ('B', 'Aa')]
        C = Converter(variables, terminals, productions)

        # Call to_cnf
        new_variables, new_terminals, new_productions = C.to_cnf(variables, terminals, productions)

        # Define expected result
        expected_productions = [('B', 'AT1'), ('S', 'T1'), ('T2', 'b'), ('X3', 'BX4'), ('S', 'T1A'), ('X4', 'B'),
                                ('B', 'T2'), ('S', 'AT1'), ('B', 'T1'), ('A', 'T1X3'), ('T1', 'a'), ('S', 'T2')]
        expected_variables = {'X4', 'T1', 'T2', 'X3', 'A', 'S', 'B'}

        # Check if the new productions and variables are equal to the expected result
        self.assertCountEqual(new_productions, expected_productions)
        self.assertCountEqual(new_variables, expected_variables)


if __name__ == '__unittest__':
    unittest.main()
