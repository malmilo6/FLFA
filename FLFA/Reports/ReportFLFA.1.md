# Laboratory Work N1. Var 6

### Course: Formal Languages & Finite Automata
### Author: Cernetchi Maxim

----

## Theory
The aim of this laboratory work was to study grammars and finite automata, which are important concepts in computer science and language theory. Grammars are used to describe the structure of languages, while finite automata are models of computation used in language recognition.
In this laboratory work, we started by studying grammars and their types, which include regular, context-free, context-sensitive, and recursive enumerable grammars. We learned about the Chomsky hierarchy, which categorizes grammars based on their generative power.
I then implemented a simple finite automaton using Python. 
## Objectives:

* To gain an understanding of the concept of grammars and their types, including regular, context-free, context-sensitive, and recursive enumerable grammars.
* To understand the concept of finite automata and their properties and limitations.
* To learn how to convert a grammar to an equivalent finite automaton.
* To implement Grammar and FA in programming language.




## Implementation description

* You can find below a Grammar class. There is literally 4 methods, including the constructor. The methods are used for generating the words following grammar rules. One method concatenates the word, and another one if for getting the symbols from transition rules.
The last method is for creating the instance of FA class, using Grammar data. I'm passing transitions, initial state, and possible final states.
```
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

```

* Here is the FA Class. The purpose is to validate the string from given Grammar. 
It gets the data from Grammar through the constructor. It needs the states(initial and final), 
and the transition rules. It takes the 1st symbol of the word and search through transitions for 
the same rule. If the current state and symbol matches the first 2 elements from transition - we are 
on the right way, then assigning the next state.
```
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
```
* Here is the main class where I instantiated the Grammar and FA.
```
def main():
    VN = ['S', 'I', 'J', 'K']
    VT = ['a', 'b', 'c', 'e', 'n', 'f', 'm']
    Transitions = [
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

    grammar = Grammar(VN, VT, Transitions, S, F)
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
```

## Conclusions 
Overall, this laboratory work was an informative and engaging introduction to the concepts of grammars and finite automata. These concepts are essential for computer science and language theory, and we now have a solid foundation to build upon in future studies.

## References
* LFPC Guide https://else.fcim.utm.md/pluginfile.php/110458/mod_resource/content/0/LFPC_Guide.pdf
* An Introduction to Formal Languages by Peter Linz, Susan H. Rodger