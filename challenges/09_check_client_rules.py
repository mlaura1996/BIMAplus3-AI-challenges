"""
Challenge 09 · The client's rules, in IDS                           ★★★

Prompt given to the AI assistant:
    "Write an IDS file for these two client rules and check MiniBIM.ifc:
     R1: every wall must say whether it is load-bearing.
     R2: the net volume of a wall must never exceed its gross volume."

The assistant wrote 09_client_rules.ids and the code below.
It runs without errors and reports that everything passes.
Your job: does each rule in the IDS really check what its name says?
What can IDS check here, and what can't it? Check R2 in Python instead.
"""
import ifcopenshell
from ifctester import ids, reporter
from _paths import MINIBIM, ROOT

model = ifcopenshell.open(MINIBIM)
spec = ids.open(str(ROOT / "challenges" / "09_client_rules.ids"))
spec.validate(model)
reporter.Console(spec).report()
