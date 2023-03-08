# Topic: Intro to formal languages. Regular grammars. Finite Automata.
## Course: Formal Languages & Finite Automata
### Author: Cernetchi Maxim
### Variant: 6
____ 
## Theory 
**Chomsky Classification**

The Chomsky Hierarchy is a classification system for formal grammars, named after the American linguist Noam Chomsky. 
It provides a way to categorize different types of formal grammars based on the types of rules they use to generate languages. 
The Chomsky Hierarchy consists of four types of grammars:

* Type 0 (Unrestricted Grammar)
* Type 1 (Context-Sensitive Grammar)
* Type 2 (Context-Free Grammar)
* Type 3 (Regular Grammar)
 
NFA and DFA are both models of computation used in computer science and formal language theory. NFA stands for Non-deterministic Finite Automaton, while DFA stands for Deterministic Finite Automaton.

A Finite Automaton is a mathematical model of a machine that reads a sequence of symbols from an input tape and changes its state based on the symbols it reads. An NFA can be in multiple states at once and can transition to multiple states based on the same symbol, while a DFA can only be in one state at a time and can transition to only one state for each symbol.

## Objectives:
1. Understand what an automaton is and what it can be used for.


2. Continuing the work in the same repository and the same project, the following need to be added:
    a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy. 

    b. For this you can use the variant from the previous lab.


3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

    a. Implement conversion of a finite automaton to a regular grammar.
    
    b. Determine whether your FA is deterministic or non-deterministic.
    
    c. Implement some functionality that would convert an NDFA to a DFA.
    
    d. Represent the finite automaton graphically (Optional, and can be considered as a bonus point):
    
    * You can use external libraries, tools or APIs to generate the figures/diagrams.
    
    * Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.

## Implementation description
1. **Chomsky Classification.**
    <p>The purpose of this task is to classify given grammar to right type. I created 3 method for Type 1, Type 2 and Type 3, 
   and one general for combining them. Because these types are like an onion, one type can include another, the method works 
   similarly, type of grammar is identified from the top.</p>


```
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
       
```

2. **FA converting to regular grammar.**
    <p>The operation of converting the FA to regular grammar is the same as converting grammar to FA, 
    but now we iterate through transitions, creating the set of productions.</p>

````
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
````

3. **Determine FA typpe.**
    <p>
    To determine whether an automaton is an NFA (Nondeterministic Finite Automaton) or DFA (Deterministic Finite Automaton), we need to check whether there exists more than one possible transition from a given state with a given input symbol.
    In an NFA, there can be multiple transitions from a given state with a given input symbol, whereas in a DFA, there is only one transition from a given state with a given input symbol. Therefore, if an automaton has more than one possible transition from a given state with a given input symbol, it is an NFA, otherwise it is a DFA.
   </p>

```
   def FA_type(self):
        for t in self._t:
            for tt in self._t:
                if t[0] == tt[0] and t[1] == tt[1] and t[2] != tt[2]:
                    return 'NFA'
        return 'DFA'
      
```

4. **NFA to DFA**
<p>
This code implements the NFA to DFA conversion algorithm. It creates a new DFA with the same alphabet and states as the original NFA. The algorithm uses a temporary set to keep track of new states as they are discovered during the conversion process.

Starting from the start state of the NFA, it computes the epsilon closure of that state and adds it as the start state of the DFA. It then proceeds to compute the transition function for each symbol in the alphabet by following transitions from each state in the current set to other states that can be reached via the symbol. The resulting set of states is added to the temporary set of states to be processed.

The algorithm continues in this manner, generating new states and transitions until all possible states have been explored. At each step, it adds the new states and transitions to the DFA. If a state contains any final state of the original NFA, it is marked as a final state in the DFA.

Finally, the algorithm returns the new DFA.
</p>

```
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
```

5. **Graphically representation of the finite automaton**
<p>For this task I used Graphviz Py library.
Graphviz is an open-source software tool for creating and manipulating graphs and diagrams. It provides a simple and flexible way to represent data in the form of graphs, trees, and other visualizations. Graphviz uses a simple text language to describe the graphs, which makes it easy to generate complex visualizations quickly. It can be used for a variety of applications, such as network diagrams, flowcharts, and data structures. Graphviz supports a wide range of output formats, including PNG, PDF, SVG, and others, making it easy to integrate into different applications and workflows.
</p>
<p> NFA from given variant:</p>

![NFA](/Images/nfa_g.gv.png)

<p>Obtained DFA:</p>

![DFA](/Images/dfa_g.gv.png)


----


