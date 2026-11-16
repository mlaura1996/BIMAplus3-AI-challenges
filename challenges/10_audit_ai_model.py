"""
Challenge 10 · Audit an AI-made model                               ★★★

CP1_AI_model.ifc is Complexo Pedagógico I (UMinho), an IFC model that
was generated with AI.

Prompt given to the AI assistant:
    "Write an audit script for CP1_AI_model.ifc and tell me whether
     the model is fit to be used in a project."

The assistant answered with the code below. It runs without errors and
says the model is OK. Every check it prints is true.
Your job: what did the auditor NOT check? Extend the script until it
gives an honest answer. Look at the header, the properties, the types,
the georeferencing... and back every finding with a number.
"""
import collections
import ifcopenshell
import ifcopenshell.util.element as ue
from _paths import CP1

model = ifcopenshell.open(CP1)
print(f"Schema: {model.schema}")

guids = collections.Counter(e.GlobalId for e in model.by_type("IfcRoot"))
dup = sum(1 for n in guids.values() if n > 1)
print(f"[OK] Duplicate GlobalIds: {dup}")

elements = [e for e in model.by_type("IfcElement") if not e.is_a("IfcOpeningElement")]
loose = [e for e in elements
         if not ue.get_container(e) and not ue.get_aggregate(e)]
print(f"[OK] Elements outside the spatial structure: {len(loose)} of {len(elements)}")

walls = model.by_type("IfcWall")
no_mat = [w for w in walls if not ue.get_material(w)]
print(f"[OK] Walls without material: {len(no_mat)} of {len(walls)}")

print("\nModel OK: fit for use.")
