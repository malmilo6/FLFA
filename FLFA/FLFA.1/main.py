import graphviz

from finite_automaton import FiniteAutomaton
from grammar import GrammarC
from converter import Converter


def main():
    # Variant 6
    variables = {'S', 'A', 'B', 'C', 'D'}
    terminals = {'a', 'b', 'd'}
    productions = [
        ('S', 'dB'),
        ("S", 'AC'),
        ("A", "d"),
        ("A", "dS"),
        ("A", "aBdB"),
        ("B", "a"),
        ("B", "aA"),
        ("B", "AC"),
        ("C", "bC"),
        ("C", 'ε'),
        ("D", "ab")
    ]

    # variables = {"S", "A", "B", "D", 'C'}
    # terminals = {"a", "b"}
    # productions = [("S", "a"), ("S", "aD"), ("D", "aD"), ("S", "aA"), ("S", "B"),
    #                ("A", "aBB"), ("A", "ε"), ("B", "Aa"), ("B", "b"), ("C", "aC")]
    C = Converter(variables, terminals, productions)
    C.cfg_to_cnf()
    C.print_cnf_productions()

    ##########################################
    # VN = ['S', 'I', 'J', 'K']
    # VT = ['a', 'b', 'c', 'e', 'n', 'f', 'm']
    # Productions = [
    #     ['S', 'cI'],
    #     ['I', 'bJ'],
    #     ['I', 'fI'],
    #     ['J', 'nJ'],
    #     ['J', 'cS'],
    #     ['I', 'eK'],
    #     ['K', 'nK'],
    #     ['I', 'e'],
    #     ['K', 'm']
    # ]
    #
    # S_ = 'S'
    # F_ = ['e', 'm']
    #
    # Q = ['q0', 'q1', 'q2', 'q3', 'q4']
    # E = ['a', 'b']
    # S = 'q0'
    # F = {'q4'}
    # Transitions = [
    #     ('q0', 'a', 'q1'),
    #     ('q1', 'b', 'q1'),
    #     ('q1', 'b', 'q2'),
    #     ('q2', 'b', 'q3'),
    #     ('q3', 'a', 'q1'),
    #     ('q2', 'a', 'q4')
    # ]
    #
    # test_tran = [
    #     ['', 'a', '', '', ''],
    #     ['', 'b', 'b', '', ''],
    #     ['', '', '', 'b', 'a'],
    #     ['', 'a', '', '', ''],
    #     ['', '', '', '', '']
    # ]
    #
    #
    # FA = FiniteAutomaton(Q, E, S, Transitions, F)
    # print(FA.FA_type())  # The output will be NFA
    # FAD = FA.nfa_to_dfa()
    # print(FAD.FA_type())  # The output will be DFA
    #
    # gram = GrammarC(VN, VT, Productions, F_)
    # print(gram.identify_grammar_type())  # The output will be Regular Grammar
    #
    # gramm_from_fa = FA.to_grammar() # The output will be object of type Grammar, created from FA

    # lAB 1
    # print(gg.generate())
    # FA = finite_automaton.FiniteAutomaton(Transitions, F, Q, E)
    # g = FA.to_grammar()
    # print(FA.FA_type())
    # gr = grammar.GrammarC(VN, VT, Productions, F_)
    # print(gr.identify_grammar_type())

    # grammar = Grammar(VN, VT, Productions, F)
    # finite_automaton = grammar.to_finite_automaton()
    # string_list: list[str] = []
    #
    # # Test data
    # for i in range(0, 5):
    #     string_list.append(grammar.generate())
    # for word in string_list:
    #     if finite_automaton.language_word(word):
    #         print('The word belongs to language')
    #     else:
    #         print('-')

    # LAB 2
    # # Graphic representation of FA (NFA or DFA)
    # states = FA.get_states()
    # transitions = FA.get_trasnitions()
    # final_states = FA.get_final_states()
    # start = 'q0'
    #
    # graph = graphviz.Digraph('NFA', filename='Reports/Images/nfa_g.gv', format='png')
    # graph.attr('node', shape='circle')
    # graph.attr('edge', arrowhead='normal')
    # for (state, symbol, next_state) in transitions:
    #     graph.edge(str(state), str(next_state), label=symbol)
    #
    # for final in final_states:
    #     graph.node(str(final), shape='doublecircle')
    # graph.view()


main()
