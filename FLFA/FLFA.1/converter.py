class Converter:
    def __init__(self, variables, terminals, productions):
        self.variables = variables
        self.terminals = terminals
        self.productions = productions


    def remove_inaccessible_symbols(self, variables, terminals, productions):
        # Initialize a set to store accessible variables
        accessible = set()
        # Add the start variable 'S' to the accessible set
        accessible.add('S')

        # Keep track of whether any changes have been made in the current iteration
        changed = True
        while changed:
            changed = False
            # Iterate through the productions
            for var, prod in productions:
                # If the production's left-hand side is in the accessible set
                if var in accessible:
                    # Iterate through the symbols in the production's right-hand side
                    for sym in prod:
                        # If the symbol is a variable and not already in the accessible set
                        if sym in variables and sym not in accessible:
                            # Add the variable to the accessible set
                            accessible.add(sym)
                            changed = True

        new_productions = [(var, prod) for var, prod in productions if var in accessible]
        new_variables = set(var for var in variables if var in accessible)

        return new_variables, terminals, new_productions

    def remove_epsilon_productions(self, variables, terminals, productions):
        # Initialize a set to store nullable variables (variables that can produce an empty string)
        nullable = set(var for var, prod in productions if prod == 'ε')

        # Iterate until there are no changes in the set of nullable variables
        changed = True
        while changed:
            changed = False
            # Iterate through all productions
            for var, prod in productions:
                # Check if all symbols in the production are nullable and the variable is not nullable
                if all(sym in nullable for sym in prod) and var not in nullable:
                    # Add the variable to the set of nullable variables
                    nullable.add(var)
                    changed = True

        # Initialize a list to store the new set of productions without epsilon productions
        new_productions = []
        for var, prod in productions:
            # If the production is not an epsilon production, add it to the new productions list
            if prod != 'ε':
                new_productions.append((var, prod))
            # If the production contains nullable symbols
            if any(sym in nullable for sym in prod):
                # Iterate through the production
                for i, sym in enumerate(prod):
                    # If the symbol is nullable
                    if sym in nullable:
                        # Create a new production without the nullable symbol
                        new_prod = prod[:i] + prod[i + 1:]
                        # Add the new production to the new productions list if it is valid and not a duplicate
                        if new_prod and (var, new_prod) not in new_productions and new_prod != var:
                            new_productions.append((var, new_prod))

        return variables, terminals, new_productions

    def remove_nonproductive_symbols(self, variables, terminals, productions):
        # Initialize a set to store productive variables (variables that can produce terminal strings)
        productive = set()

        # Find variables that directly produce terminals and add them to the productive set
        for var in variables:
            if any(prod in terminals for prod in productions if prod[0] == var):
                productive.add(var)

        # Iterate until there are no changes in the set of productive variables
        changed = True
        while changed:
            changed = False
            # Iterate through all productions
            for var, prod in productions:
                # Check if the variable is not productive and all symbols in the production are either productive or
                # terminals
                if var not in productive and all(sym in productive | terminals for sym in prod):
                    # Add the variable to the set of productive variables
                    productive.add(var)
                    changed = True

        # Find the nonproductive variables by subtracting the productive variables from the original set of variables
        nonproductive = variables - productive

        # Create a new set of productions without nonproductive variables
        new_productions = [prod for prod in productions if
                           prod[0] in productive and all(sym in productive | terminals for sym in prod[1])]

        # Update the set of variables by removing nonproductive variables
        new_variables = variables - nonproductive

        return new_variables, terminals, new_productions

    def remove_unit_productions(self, variables, terminals, productions):
        # Identify unit productions (productions with a single variable on the right side)
        unit_productions = {(var, prod) for var, prod in productions if len(prod) == 1 and prod in variables}
        # Identify non-unit productions
        non_unit_productions = {(var, prod) for var, prod in productions if (var, prod) not in unit_productions}
        # Initialize a set to store the new set of productions without unit productions
        new_productions = non_unit_productions.copy()

        # Iterate through all unit productions
        for var1, var2 in unit_productions:
            # Iterate through all non-unit productions
            for prod in non_unit_productions:
                # If the left side of the non-unit production matches the right side of the unit production
                if prod[0] == var2:
                    # Add a new production with the left side of the unit production and the right side of the non-unit production
                    new_productions.add((var1, prod[1]))

        return variables, terminals, list(new_productions)

    def to_cnf(self, variables, terminals, productions):
        new_productions = []
        next_new_var = 1
        terminal_var_map = {}
        prod_var_map = {}

        for var, prod in productions:
            if len(prod) >= 3:
                if prod not in prod_var_map:
                    prod_vars = [f"X{next_new_var + i}" for i in range(len(prod) - 2)]
                    next_new_var += len(prod) - 2
                    variables.update(prod_vars)
                    prod_var_map[prod] = prod_vars

                prod_vars = prod_var_map[prod]

                new_productions.append((var, prod[0] + prod_vars[0]))
                for i in range(len(prod) - 3):
                    new_productions.append((prod_vars[i], prod[i + 1] + prod_vars[i + 1]))
                new_productions.append((prod_vars[-1], prod[-2:]))

            elif len(prod) == 2 and all(sym in variables for sym in prod):
                new_productions.append((var, prod))

            else:
                new_prod = prod
                for sym in prod:
                    if sym in terminals:
                        if sym not in terminal_var_map:
                            new_var = f"T{next_new_var}"
                            next_new_var += 1
                            variables.add(new_var)
                            new_productions.append((new_var, sym))
                            terminal_var_map[sym] = new_var
                        new_prod = new_prod.replace(sym, terminal_var_map[sym], 1)
                new_productions.append((var, new_prod))

        return variables, terminals, new_productions

    def cfg_to_cnf(self):
        self.variables, self.terminals, self.productions = self.remove_epsilon_productions(self.variables, self.terminals, self.productions)
        self.variables, self.terminals, self.productions = self.remove_unit_productions(self.variables, self.terminals, self.productions)
        self.variables, self.terminals, self.productions = self.remove_inaccessible_symbols(self.variables, self.terminals, self.productions)
        self.variables, self.terminals, self.productions = self.remove_nonproductive_symbols(self.variables, self.terminals, self.productions)
        self.variables, self.terminals, self.productions = self.to_cnf(self.variables, self.terminals, self.productions)
        return self.variables, self.terminals, self.productions

    def print_cnf_productions(self):
        grouped_productions = {}
        for var, prod in self.productions:
            if var not in grouped_productions:
                grouped_productions[var] = [prod]
            else:
                grouped_productions[var].append(prod)

        print("Variables:", self.variables)
        print("Terminals:", self.terminals)
        print("Productions:")
        for var, prods in grouped_productions.items():
            print(f"{var} -> {' | '.join(prods)}")

