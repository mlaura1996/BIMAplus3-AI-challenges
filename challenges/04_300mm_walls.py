"""
Challenge 04 · How many 300 mm walls?                                ★★

Prompt given to the AI assistant:
    "How many walls in MiniBIM.ifc are exactly 300 mm thick?
     Use the Width in Qto_WallBaseQuantities."

The assistant answered with the code below. It runs without errors.
Your job: PREDICT the output, RUN it, find what is WRONG, FIX it,
and EXPLAIN in one sentence why the AI got it wrong.
Hint for the check: count the same walls in a second, independent way.
"""
import ifcopenshell
import ifcopenshell.util.element
from _paths import MINIBIM

model = ifcopenshell.open(MINIBIM)

count = 0
for wall in model.by_type("IfcWall"):
    qto = ifcopenshell.util.element.get_psets(wall)["Qto_WallBaseQuantities"]
    if qto["Width"] == 0.3:        # 300 mm, the file is in metres
        count += 1

print(f"{count} walls are 300 mm thick.")
