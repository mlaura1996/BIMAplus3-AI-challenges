"""Shared paths. Put MiniBIM.ifc in the data/ folder (see data/README.md)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MINIBIM = str(ROOT / "data" / "MiniBIM.ifc")
OUT = ROOT / "out"
OUT.mkdir(exist_ok=True)

# Our wall: the façade wall from BIM A+2, "Anatomy of an IfcWall"
WALL = "2pjBMhmIb9UvPqt$wR2ogX"
