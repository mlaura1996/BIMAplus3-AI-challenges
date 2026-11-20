"""
Question 6 · Delete the basement

The request:
    "Remove everything on the basement storey (-1 kelder) of MiniBIM.ifc
     and save the result as a new file."

This script was written for that request. It runs without errors and
the new file opens in a viewer.
Your task: predict, run, check, fix or defend, explain.
- The new file opens in a viewer. Is anything left behind? Count it.
- If something is left, rewrite the script so that nothing is, and
  prove it with the same counts.
"""
import ifcopenshell
from _paths import MINIBIM, OUT

model = ifcopenshell.open(MINIBIM)

basement = next(s for s in model.by_type("IfcBuildingStorey")
                if s.Name.startswith("-1"))

removed = 0
for rel in basement.ContainsElements:
    for element in list(rel.RelatedElements):
        model.remove(element)
        removed += 1

model.write(str(OUT / "MiniBIM_no_basement.ifc"))
print(f"Removed {removed} elements. Basement deleted.")
