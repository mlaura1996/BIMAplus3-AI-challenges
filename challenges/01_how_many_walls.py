"""
Question 1 · How many walls?

The request:
    "Count the walls in MiniBIM.ifc."

This script was written for that request. It runs without errors.
Your task: predict what it prints, run it, check the answer a second,
independent way, fix it or defend it, and explain in one sentence.
- How many walls does the model have? Is our wall one of them?
- Why might someone choose IfcWallStandardCase instead of IfcWall?
"""
import ifcopenshell
from _paths import MINIBIM

model = ifcopenshell.open(MINIBIM)

# IfcWallStandardCase is the standard class for walls in IFC
walls = model.by_type("IfcWallStandardCase")

print(f"The model contains {len(walls)} walls.")
