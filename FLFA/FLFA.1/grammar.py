import random

# from finite_automaton import FiniteAutomaton
import finite_automaton


class GrammarC:

    def __init__(self, vn, vt, p, f):
        self._vn = vn
        self._vt = vt
        self._p = p
        self._s = self._p[0][0]
        self._f = f

    def help_generate(self, symbol) -> str:
        word: str = ''
        possible_productions: list = []

        # # There are many possibilities of transactions with the same first symbol,
        # # I decided to group them together and choose one randomly
        # for production in self._p:
        #     if symbol in production[0]:
        #         possible_transitions.append(production)
        # random_production = random.randint(0, len(possible_transitions) - 1)
        #
        # # As there are transactions with final state, I check for them to avoid index error
        # if len(possible_transitions[random_production]) == 3:
        #     word += possible_transitions[random_production][1] + possible_transitions[random_production][2]
        # else:
        #     word += possible_transitions[random_production][1]
        # return word

        for production in self._p:
            if symbol == production[0]:
                possible_productions.append(production)
        random_production = random.randint(0, len(possible_productions)-1)
        word += possible_productions[random_production][1]
        return word

    def get_state(self):
        return self._s

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

    def identify_grammar_type(self):
        state = ''
        if self.type_3():
            state = 'Regular Grammar'
        elif self.type_2():
            state = 'Context-free grammar'
        elif self.type_1():
            state = 'Context-sensitive grammar'
        else:
            state = 'Unrestricted grammar'
        return state

    def type_3(self):
        state: bool = False
        for p in self._p:
            lhs = p[0]
            rhs = p[1]
            if len(lhs) == 1 and lhs[0].isupper():
                if (len(rhs) == 1 and rhs[0].islower()) or (len(rhs) == 2 and rhs[0].islower() and rhs[1].isupper()):
                    state = True
                else:
                    state = False
                    break
            else:
                state = False
                break
        return state

    def type_2(self):
        state: bool = False
        for p in self._p:
            lhs = p[0]
            rhs = p[1]
            if len(lhs) == 1 and lhs[0].isupper():
                if len(rhs) > 2:
                    state = True
                    break
                else:
                    state = False
        return state

    def type_1(self):
        state: bool = True
        for p in self._p:
            lhs = p[0]
            rhs = p[1]
            for symbol in lhs:
                if symbol.islower() and len(lhs) > 3:
                    state = False
                    break
        return state

    def productions_to_transitions(self):
        transitions = []
        for p in self._p:
            if len(p[1]) == 2:
                transitions.append([p[0], str(p[1])[0], str(p[1])[1]])
            else:
                transitions.append([p[0], p[1]])
        return transitions

    # Call the constructor for FA and pass the grammar
    def to_finite_automaton(self):
        return finite_automaton.FiniteAutomaton(
            self._vn,
            self._vt,
            self._s,
            self.productions_to_transitions(),
            self._f
        )
