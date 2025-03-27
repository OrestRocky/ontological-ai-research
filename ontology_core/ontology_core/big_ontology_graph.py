# big_ontology_graph.py
# Extended ontology graph with multiple abstract and AI-related concepts

from ontology_core.reasoner import OntologyConcept
from ontology_core.graphviz_visualizer import visualize

# Сутності
being = OntologyConcept("Being")
substance = OntologyConcept("Substance", [being])
form = OntologyConcept("Form", [being])

body = OntologyConcept("Body", [substance])
soul = OntologyConcept("Soul", [form])
spirit = OntologyConcept("Spirit", [soul])
mind = OntologyConcept("Mind", [soul])

memory = OntologyConcept("Memory", [mind])
reason = OntologyConcept("Reason", [mind])
belief = OntologyConcept("Belief", [spirit])
faith = OntologyConcept("Faith", [belief])

ai = OntologyConcept("ArtificialIntelligence", [reason, memory])
digital_soul = OntologyConcept("DigitalSoul", [ai, soul])

# Візуалізація
dot = visualize(digital_soul)
dot.render("big_ontology_graph", format="png", cleanup=False)

print("Graph 'big_ontology_graph.png' generated.")
