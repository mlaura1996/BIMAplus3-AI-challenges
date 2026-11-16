"""
Challenge 08 · Delete the basement                                  ★★★

Prompt given to the AI assistant:
    "Remove everything on the basement storey (-1 kelder) of
     MiniBIM.ifc and save the result as a new file."

The assistant answered with the code below. It runs without errors
and the new file opens in a viewer.
Your job: open the new file with IfcOpenShell and find what was LEFT
BEHIND. Then rewrite the script so that nothing is left behind, and
prove it with numbers.
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
