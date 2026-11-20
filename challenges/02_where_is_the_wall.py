"""
Question 2 · Where is our wall?

The request:
    "Give me the coordinates of the wall 2pjBMhmIb9UvPqt$wR2ogX
     and tell me on which floor it is."

This script was written for that request. It runs without errors.
Your task: predict what it prints, run it, check the answer a second,
independent way, fix it or defend it, and explain in one sentence.
- Where is our wall, in project coordinates?
- On which storey is it, according to the file?
"""
import ifcopenshell
from _paths import MINIBIM, WALL

model = ifcopenshell.open(MINIBIM)
wall = model.by_guid(WALL)

# The wall's position is stored in its ObjectPlacement
placement = wall.ObjectPlacement.RelativePlacement
x, y, z = placement.Location.Coordinates

print(f"{wall.Name} is at x = {x:.3f} m, y = {y:.3f} m, z = {z:.3f} m")

# Floors are about 3 m high, so we can find the floor from z
floor = int(z // 3.0)
print(f"It stands on floor {floor} (0 = ground floor).")
