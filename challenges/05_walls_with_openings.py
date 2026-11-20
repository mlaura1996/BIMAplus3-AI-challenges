"""
Question 4 · Which walls have an opening?

The request:
    "List the walls in MiniBIM.ifc that have at least one opening
     (a door or a hole)."

This script was written for that request. It runs without errors.
Your task: predict what it prints, run it, check the answer a second,
independent way, fix it or defend it, and explain in one sentence.
- How many walls have at least one opening?
- Is there another way to check whether a wall has an opening?
- What do NetVolume and GrossVolume mean? When could they be wrong?
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
