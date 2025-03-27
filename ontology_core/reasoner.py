# reasoner.py
# Simple symbolic reasoner for concept hierarchy

class Concept:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def is_a(self, concept_name):
        if self.name == concept_name:
            return True
        elif self.parent:
            return self.parent.is_a(concept_name)
        return False

# Example
human = Concept("Human", Concept("Mammal", Concept("Animal")))
print(human.is_a("Animal"))  # True
