"""
Question 5 · Doors per storey

The request:
    "For each storey of MiniBIM.ifc, count the doors."

This script was written for that request. It runs without errors.
Your task: predict what it prints, run it, check the answer a second,
independent way, fix it or defend it, and explain in one sentence.
- How many doors are there on each storey? And on the storey of our wall?
- Do your storey counts add up to the total number of doors?
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
