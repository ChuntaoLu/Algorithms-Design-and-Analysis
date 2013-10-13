import math
import random
from time import time
from itertools import chain
from collections import defaultdict

def papa(clause_pairs):
    """
    Papadimitriou's 2SAT algorithm using the principle of local search.
    
    Pick a random assignment of the variables and test the satisfiability,
    if satisfied return satisfiable, otherwise randomly choose a failed
    clause and randomly choose one of its two variable and flip its value.
    """
    variables = set(map(abs, chain(*clause_pairs)))
    num_of_repeat = int(math.log(len(variables), 2))
    for i in range(num_of_repeat):
        assign = {}
        for var in variables:
            assign[var] = random.choice([True, False])
            assign[-var] = not assign[var]
        for j in range(2 * pow(len(variables), 2)):
            false_clause_pairs = pick_false_clause(clause_pairs, assign)
            if false_clause_pairs == []:
                return 1
            else:
                chosen_clause = random.choice(false_clause_pairs)
                chosen_var = abs(random.choice(chosen_clause))
                assign[chosen_var] = not assign[chosen_var]
                assign[-chosen_var] = not assign[chosen_var]
    return 0


def pick_false_clause(clause_pairs, assign):
    """Given the assignment of each variable, return a list of the clauses
    that are not satisfied. Empty list means 2SAT is satisfied.

    'clause_pairs' in form of set((variable1, variable2), ...)
    'assign' in form of {variable: boolean, ...}."""

    return [x for x in clause_pairs if not (assign[x[0]] | assign[x[1]])]

def reduce_clause(all_clause_pairs):
    """Given all the clauses of a 2SAT problem, remove the clauses that include
    a variable which has only one form (itself or its negation) in all clauses.
    Because of the singular form of such variables, having the form to be true
    means having the clauses containing this form to be true, thus those clauses
    can be removed without affecting the original 2SAT problem.

    For example:
    1, -3
    2, 1
    1, 4
    -2, 3
    -3, 2
    can be reduced to
    -2, 3
    -3, 2
    because variable 1 has on negation in all clauses, we just set it to be true,
    then the first three clauses are true and can be ignored.

    Note that after one iteration of reduction, some variables that are not
    singular prior to reduction can become singular afterwards, thus reduction
    should be done iteratively until no singular variables exist.
    
    'var_clause_dict' in forms of {variable:set(clause, ...), ...} shows all
    clauses containing that variable for each variable, a clause in an entry
    gets removed if either of its variables is singular.
    
    'clause_var_dict' in forms of {clause:[variable, variable], ...} shows the
    two variables involved in that clause for each clause, an entry gets removed
    if either of its variables is singular.
    
    Reduction in 'var_clause_dict' and 'clause_var_dict' MUST be in sync. After
    each reduction iteration, the values of 'clause_var_dict' are the remaining
    variables and the keys of 'var_clause_dict' are the remaining clauses.

    https://class.coursera.org/algo2-002/forum/thread?thread_id=431#post-1601
    """

    singular_var = set()
    clause_var_dict = {} 
    var_clause_dict = defaultdict(set)
    for x, y in all_clause_pairs:
        var_clause_dict[x].add((x, y))
        var_clause_dict[y].add((x, y))
        clause_var_dict[(x,y)] = [x, y]
    while True:
        for var in singular_var:
            for clause in var_clause_dict[var].copy():
                del clause_var_dict[clause]
                var_clause_dict[clause[0]] -= set([clause])
                var_clause_dict[clause[1]] -= set([clause])
        reduced_var = set(chain(*clause_var_dict.values()))
        singular_var = set([i for i in reduced_var if -i not in reduced_var])
        if singular_var == set():
            break
    return set(clause_var_dict.keys())
 

def main():
    out = []
    for i in range(1, 7):
        all_clause_pairs = set()
        with open('2sat%s.txt' % i) as file_in:
        #with open('test.txt') as file_in:
            next(file_in)
            for line in file_in:
                x, y = map(int, line.strip().split(' '))
                all_clause_pairs.add((x, y))
        reduced_clause_pairs = reduce_clause(all_clause_pairs)
        print len(reduced_clause_pairs)
        out.append(papa(reduced_clause_pairs))
    return out


if __name__ == "__main__":
    start = time()
    print main()
    print time() - start
