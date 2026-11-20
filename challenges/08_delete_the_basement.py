"""
Question 6 · Delete the basement

The request:
    "Remove everything on the basement storey named "-1 kelder" of
     MiniBIM.ifc and save the result as a new file."

This script was written for that request. It runs without errors.
Your task: predict, run, check, fix or defend, explain.
- Open the new file in a viewer. Is anything left behind? Count it.
- If something is left, rewrite the script so that nothing is, and
  check again in the viewer.
"""
import ifcopenshell
from _paths import MINIBIM, OUT

model = ifcopenshell.open(MINIBIM)

basement = [s for s in model.by_type("IfcBuildingStorey")
            if s.Name.startswith("-1")][0]

removed = 0
for rel in basement.ContainsElements:
    for element in list(rel.RelatedElements):
        model.remove(element)
        removed += 1

model.write(str(OUT / "MiniBIM_no_basement.ifc"))
print(f"Removed {removed} elements. Basement deleted.")
