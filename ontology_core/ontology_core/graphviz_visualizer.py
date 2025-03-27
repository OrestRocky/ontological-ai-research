# graphviz_visualizer.py
# Visualization of ontology tree using Graphviz

from ontology_core.reasoner import OntologyConcept
from graphviz import Digraph

def visualize(concept: OntologyConcept, dot=None, visited=None):
    if dot is None:
        dot = Digraph()
    if visited is None:
        visited = set()

    if concept.name in visited:
        return dot
    visited.add(concept.name)

    for parent in concept.parents:
        dot.edge(parent.name, concept.name)
        visualize(parent, dot, visited)

    return dot

# Example
animal = OntologyConcept("Animal")
mammal = OntologyConcept("Mammal", [animal])
human = OntologyConcept("Human", [mammal])
ai = OntologyConcept("AIEntity", [human])

dot = visualize(ai)
dot.render("ontology_graph", format="png", cleanup=False)  # Generates ontology_graph.png
