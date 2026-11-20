"""
Question 3 · How many walls like ours?

The request:
    "Our wall is 300 mm thick. How many walls in MiniBIM.ifc are exactly
     300 mm thick? Use the Width in Qto_WallBaseQuantities."

This script was written for that request. It runs without errors.
Your task: predict what it prints, run it, check the answer a second,
independent way, fix it or defend it, and explain in one sentence.
- How many 300 mm walls are there?
- Count them a second, independent way. Do the two numbers agree?
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
