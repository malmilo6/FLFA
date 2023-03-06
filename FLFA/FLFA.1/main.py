from grammar import Grammar


def main():
    VN = ['S', 'I', 'J', 'K']
    VT = ['a', 'b', 'c', 'e', 'n', 'f', 'm']
    Productions = [
        ['S', 'c', 'I'],
        ['I', 'b', 'J'],
        ['I', 'f', 'I'],
        ['J', 'n', 'J'],
        ['J', 'c', 'S'],
        ['I', 'e', 'K'],
        ['K', 'n', 'K'],
        ['I', 'e'],
        ['K', 'm']
    ]

    S = 'S'
    F = ['e', 'm']

    grammar = Grammar(VN, VT, Productions, S, F)
    finite_automaton = grammar.to_finite_automaton()
    string_list: list[str] = []

    # Test data
    for i in range(0, 5):
        string_list.append(grammar.generate())
    for word in string_list:
        if finite_automaton.language_word(word):
            print('The word belongs to language')
        else:
            print('-')

main()
