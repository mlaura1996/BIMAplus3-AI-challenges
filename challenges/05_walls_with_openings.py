"""
Challenge 05 · Which walls have an opening?                          ★★

Prompt given to the AI assistant:
    "List the walls in MiniBIM.ifc that have at least one opening
     (a door or a hole)."

The assistant answered with the code below. It runs without errors.
Your job: PREDICT the output, RUN it, find what is WRONG, FIX it,
and EXPLAIN in one sentence why the AI got it wrong.
"""
import ifcopenshell
import ifcopenshell.util.element
from _paths import MINIBIM

model = ifcopenshell.open(MINIBIM)

with_openings = []
for wall in model.by_type("IfcWall"):
    qto = ifcopenshell.util.element.get_psets(wall)["Qto_WallBaseQuantities"]
    # An opening removes material, so the net volume is smaller
    # than the gross volume.
    if qto["NetVolume"] < qto["GrossVolume"]:
        with_openings.append(wall)

print(f"{len(with_openings)} walls have at least one opening.")
