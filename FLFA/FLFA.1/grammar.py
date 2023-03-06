import random

from finite_automaton import FiniteAutomaton


class Grammar:

    def __init__(self, vn, vt, p, s, f):
        self._vn = vn
        self._vt = vt
        self._p = p
        self._s = s
        self._f = f

    def help_generate(self, symbol) -> str:
        word: str = ''
        possible_transitions: list = []

        # for production in self._p:
        #     if symbol in production[0]:
        #         random_production = random.randint(1, len(production) - 1)
        #         word += production[random_production]
        # return word

        # There are many possibilities of transactions with the same first symbol,
        # I decided to group them together and choose one randomly
        for transition in self._p:
            if symbol in transition[0]:
                possible_transitions.append(transition)
        random_transition = random.randint(0, len(possible_transitions) - 1)

        # As there are transactions with final state, I check for them to avoid index error
        if len(possible_transitions[random_transition]) == 3:
            word += possible_transitions[random_transition][1] + possible_transitions[random_transition][2]
        else:
            word += possible_transitions[random_transition][1]
        return word

    def generate(self) -> str:
        # Declaring final states and beginning of the word
        F = self._f
        word = self._s

        # Saving last symbol of the word to parse it into the helper function
        last_symbol = str(word[len(word) - 1])
        while last_symbol not in F:
            word = word[:-1]
            word += self.help_generate(last_symbol)
            last_symbol = str(word[len(word) - 1])
        return word

    # Call the constructor for FA and pass the grammar
    def to_finite_automaton(self) -> FiniteAutomaton:

        return FiniteAutomaton(self._p, self._s, self._f)
