class Forward_Chaining:
    def __init__(self):
        self.facts = set()
        self.rules = []
        
    def add(self, fact=None, condition=None, conclusion=None):
        if fact : self.facts.add(fact)
        elif condition and conclusion : self.rules.append((condition, conclusion))

    def infer(self):
        while True:
            new_facts = False
            for condition, conclusion in self.rules:
                if condition.issubset(self.facts) and conclusion not in self.facts:
                    self.facts.add(conclusion)
                    new_facts = True
                    print(f"Added fact: {conclusion} from rule {condition} -> {conclusion}")
            if not new_facts:
                break

    def get_facts(self):
        return self.facts

if __name__ == "__main__":
    fc = Forward_Chaining()
    fc.add(fact="Fever")
    fc.add(fact="Cough")
    fc.add(condition={"Fever", "Cough"}, conclusion="Possible Influenza")
    fc.add(condition={"Fever"}, conclusion="Possible Feverish Condition")
    fc.add(condition={"Cough"}, conclusion="Possible Respiratory Issue")

    fc.infer()
    print("-----")
    for fact in fc.get_facts():
        print(fact)