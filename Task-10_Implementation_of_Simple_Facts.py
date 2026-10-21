# Task 10: Implementation of Simple Facts using Python

class SimpleKB:
    def __init__(self): 
        self.facts = set()

    def add(self, p, *args): 
        self.facts.add((p, args))

    def infer(self):
        # Grandparent rule: parent(X, Y) and parent(Y, Z) => grandparent(X, Z)
        parents = [args for p, args in self.facts if p == "parent"]
        for x, y in parents:
            for y2, z in parents:
                if y == y2: self.facts.add(("grandparent", (x, z)))
        # Father rule: parent(X, Y) and male(X) => father(X, Y)
        males = [args[0] for p, args in self.facts if p == "male"]
        for x, y in parents:
            if x in males: self.facts.add(("father", (x, y)))

    def query(self, p, *args): 
        return (p, args) in self.facts

kb = SimpleKB()
kb.add("parent", "John", "Mary")
kb.add("parent", "Mary", "Alice")
kb.add("male", "John")
kb.infer()

for q in [("parent", "John", "Mary"), ("father", "John", "Mary"), ("grandparent", "John", "Alice"), ("father", "Mary", "Alice")]:
    print(f"{q[0]}({', '.join(q[1:])}) -> {kb.query(*q)}")

# Output:
# parent(John, Mary) -> True
# father(John, Mary) -> True
# grandparent(John, Alice) -> True
# father(Mary, Alice) -> False
