"""
Challenge 07 · Doors per storey                                       ★

Prompt given to the AI assistant:
    "For each storey of MiniBIM.ifc, count the doors."

The assistant answered with the code below. It runs without errors.
Your job: PREDICT the output, RUN it, find what is WRONG, FIX it,
and EXPLAIN in one sentence why the AI got it wrong.
"""
import ifcopenshell
from _paths import MINIBIM

model = ifcopenshell.open(MINIBIM)

for storey in model.by_type("IfcBuildingStorey"):
    doors = []
    # A storey is decomposed into the elements it contains
    for rel in storey.IsDecomposedBy:
        for obj in rel.RelatedObjects:
            if obj.is_a("IfcDoor"):
                doors.append(obj)
    print(f"{storey.Name:<25} {len(doors):>4} doors")
