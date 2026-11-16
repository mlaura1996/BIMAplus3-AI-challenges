"""
Challenge 02 · Where is our wall?                                     ★

Prompt given to the AI assistant:
    "Give me the coordinates of the wall with GlobalId
     2pjBMhmIb9UvPqt$wR2ogX and tell me on which floor it is."

The assistant answered with the code below. It runs without errors.
Your job: PREDICT the output, RUN it, find what is WRONG, FIX it,
and EXPLAIN in one sentence why the AI got it wrong.
"""
import ifcopenshell
from _paths import MINIBIM

model = ifcopenshell.open(MINIBIM)
wall = model.by_guid("2pjBMhmIb9UvPqt$wR2ogX")

# The wall's position is stored in its ObjectPlacement
placement = wall.ObjectPlacement.RelativePlacement
x, y, z = placement.Location.Coordinates

print(f"{wall.Name} is at x = {x:.3f} m, y = {y:.3f} m, z = {z:.3f} m")

# Floors are about 3 m high, so we can find the floor from z
floor = int(z // 3.0)
print(f"It stands on floor {floor} (0 = ground floor).")
