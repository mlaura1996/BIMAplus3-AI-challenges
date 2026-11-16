"""
Challenge 01 · How many walls?                                        ★

Prompt given to the AI assistant:
    "Write a Python script with IfcOpenShell that counts the walls
     in MiniBIM.ifc."

The assistant answered with the code below. It runs without errors.
Your job: PREDICT the output, RUN it, find what is WRONG, FIX it,
and EXPLAIN in one sentence why the AI got it wrong.
"""
import ifcopenshell
from _paths import MINIBIM

model = ifcopenshell.open(MINIBIM)

# IfcWallStandardCase is the standard class for walls in IFC
walls = model.by_type("IfcWallStandardCase")

print(f"The model contains {len(walls)} walls.")
