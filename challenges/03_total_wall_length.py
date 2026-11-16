"""
Challenge 03 · How many metres of wall?                              ★★

Prompt given to the AI assistant:
    "Sum the length of all walls in MiniBIM.ifc and give me the total
     in metres."

The assistant answered with the code below. It runs without errors.
Your job: PREDICT the output, RUN it, find what is WRONG, FIX it,
and EXPLAIN in one sentence why the AI got it wrong.
"""
import ifcopenshell
import ifcopenshell.util.element
from _paths import MINIBIM

model = ifcopenshell.open(MINIBIM)

total_mm = 0.0
for wall in model.by_type("IfcWall"):
    psets = ifcopenshell.util.element.get_psets(wall)
    total_mm += psets["Qto_WallBaseQuantities"]["Length"]

# IFC files exported from Revit store lengths in millimetres
total_m = total_mm / 1000
print(f"Total wall length: {total_m:.2f} m")
