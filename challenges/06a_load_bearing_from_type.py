"""
Challenge 06 · Two scripts, two answers (script A)                   ★★

Prompt given to the AI assistant (twice, in two different chats):
    "How many load-bearing walls are there in MiniBIM.ifc?"

This is the first answer. Run 06b too. Both run without errors.
Your job: which number does the FILE actually say, and why?
Which number would a structural engineer expect? What would you
report back to the modeller?
"""
import ifcopenshell
import ifcopenshell.util.element
from _paths import MINIBIM

model = ifcopenshell.open(MINIBIM)

n = 0
for wall in model.by_type("IfcWall"):
    # Properties shared by all walls of the same kind live on the type
    wall_type = ifcopenshell.util.element.get_type(wall)
    psets = ifcopenshell.util.element.get_psets(wall_type)
    if psets.get("Pset_WallCommon", {}).get("LoadBearing"):
        n += 1

print(f"Script A: {n} load-bearing walls.")
