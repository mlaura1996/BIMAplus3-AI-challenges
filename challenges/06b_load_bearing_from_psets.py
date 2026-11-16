"""
Challenge 06 · Two scripts, two answers (script B)                   ★★

Prompt given to the AI assistant (twice, in two different chats):
    "How many load-bearing walls are there in MiniBIM.ifc?"

This is the second answer. Compare it with 06a.
"""
import ifcopenshell
import ifcopenshell.util.element
from _paths import MINIBIM

model = ifcopenshell.open(MINIBIM)

n = 0
for wall in model.by_type("IfcWall"):
    psets = ifcopenshell.util.element.get_psets(wall)
    if psets.get("Pset_WallCommon", {}).get("LoadBearing"):
        n += 1

print(f"Script B: {n} load-bearing walls.")
