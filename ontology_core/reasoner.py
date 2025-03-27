# reasoner.py
# Refactored symbolic reasoner with multiple inheritance support

class OntologyConcept:
    def __init__(self, name, parents=None):
        self.name = name
        self.parents = parents if parents else []

    def is_a(self, concept_name):
        if self.name == concept_name:
            return True
        for parent in self.parents:
            if parent.is_a(concept_name):
                return True
        return False

# Examples
animal = OntologyConcept("Animal")
mammal = OntologyConcept("Mammal", [animal])
human = OntologyConcept("Human", [mammal])
soul = OntologyConcept("Soul")
ai_entity = OntologyConcept("AIEntity", [human, soul])

print(ai_entity.is_a("Animal"))  # True
print(ai_entity.is_a("Soul"))    # True
