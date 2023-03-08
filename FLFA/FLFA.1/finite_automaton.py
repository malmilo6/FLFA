import grammar


# Helping functions to get the sets from frozenset
def trans_to_set(f):
    ff = [(set(s1), sym, set(s2)) for s1, sym, s2 in f]
    return ff


def frozen_to_set(f):
    frozen = list(f)
    result = [tuple(set_item) for set_item in frozen]
    return result


class FiniteAutomaton:

    def __init__(self, Q, E, S, T, F):
        self._t = T
        self._s = S
        self._f = F
        self._q = Q
        self._e = E

    def language_word(self, word) -> bool:

        # Initialising first symbol with 'S'
        current_state = self._s

        for character in word:
            next_state = 'empaty'
            for transition in self._t:
                # Check if it's matching the needed transition
                if transition[0] == current_state and transition[1] == character:
                    next_state = transition[len(transition) - 1]
                    break
            # If next state is empty, the word doesn't match the rule
            if next_state == 'empaty':
                return False
            current_state = next_state
        return True

    def to_grammar(self):
        # VN and VT remain the same, but Transitions have to be converted into Productions
        V_N = self._q
        V_T = self._e
        Productions = self.transition_to_production()
        F = self._f
        return grammar.GrammarC(V_N, V_T, Productions, F)

    # Method for converting Transitions to Productions
    def transition_to_production(self):
        productions = []
        for t in self._t:
            productions.append([t[0], t[1] + t[2]])
        return productions

    # FA identification method. If there are 2 or more paths leading to different edges from one, than it's NFA
    def FA_type(self):
        for t in self._t:
            for tt in self._t:
                if t[0] == tt[0] and t[1] == tt[1] and t[2] != tt[2]:
                    return 'NFA'
        return 'DFA'

    # Method for converting NFA to DFA
    def nfa_to_dfa(self):
        # Initialising lists for DFA states, transitions, final states
        dfa_states = []
        dfa_transitions = []
        dfa_start_state = frozenset([self._s])
        dfa_final_states = set()

        temp_current_states = [dfa_start_state]
        temp_states = {dfa_start_state}

        # Iterating through current states until we get all possible new states
        while len(temp_current_states) > 0:
            current_states = temp_current_states.pop(0)
            dfa_states.append(current_states)

            for symbol in self._e:
                next_states = set()
                for state in current_states:
                    for transition in self._t:
                        if transition[0] == state and transition[1] == symbol:
                            next_states.add(transition[2])

                if not next_states:
                    continue

                next_states = frozenset(next_states)

                if next_states not in temp_states:
                    temp_states.add(next_states)
                    temp_current_states.append(next_states)

                dfa_transitions.append((current_states, symbol, next_states))

                if any(state in next_states for state in self._f):
                    dfa_final_states.add(next_states)

        return FiniteAutomaton(frozen_to_set(dfa_states), self._e, frozen_to_set(dfa_start_state),
                               trans_to_set(dfa_transitions), frozen_to_set(dfa_final_states))

    def get_states(self):
        return self._q

    def get_final_states(self):
        return self._f

    def get_start_state(self):
        return self._s

    def get_trasnitions(self):
        return self._t