
class FiniteAutomaton:

    def __init__(self, p, s, f):
        self._p = p
        self._s = s
        self._f = f

    def language_word(self, word) -> bool:

        # Initialising first symbol with 'S'
        current_state = self._s

        for character in word:
            next_state = 'empaty'
            for transition in self._p:
                # Check if it's matching the needed transition
                if transition[0] == current_state and transition[1] == character:
                    next_state = transition[len(transition)-1]
                    break
            # If next state is empty, the word doesn't match the rule
            if next_state == 'empaty':
                return False
            current_state = next_state
        return True






