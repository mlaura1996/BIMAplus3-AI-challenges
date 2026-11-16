"""Shared paths. Put the two IFC files in the data/ folder (see data/README.md)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MINIBIM = str(ROOT / "data" / "MiniBIM.ifc")
CP1 = str(ROOT / "data" / "CP1_AI_model.ifc")
OUT = ROOT / "out"
OUT.mkdir(exist_ok=True)
