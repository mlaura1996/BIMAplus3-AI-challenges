# One model, six questions

**BIM A+3 · Parametric modelling in BIM · Topic 3: Programming applied to IFC**
Hands-on challenges, 2026/2027

The script runs. Is the answer right?

One building, one wall, six questions. For each question you get a request and a Python script written for it. Every script runs without errors.

## How it works

For each question:

1. **Predict** what the script will print, before you run it.
2. **Run** it on the model.
3. **Check** the answer a second, independent way.
4. **Fix or defend.** Some scripts need a fix; some answers depend on how you read the file. Decide, and say why.
5. **Explain** in one sentence, and back it with a number.

Use any tool you like, AI included. You sign the answer.

Write your answers in `WORKSHEET.md`. At the end, we pick one line of your code and you defend it in two minutes.

## The questions

| # | Question | Script |
|---|---|---|
| 1 | How many walls? | `challenges/01_how_many_walls.py` |
| 2 | Where is our wall? | `challenges/02_where_is_the_wall.py` |
| 3 | How many walls like ours? | `challenges/03_walls_like_ours.py` |
| 4 | Which walls have an opening? | `challenges/04_walls_with_openings.py` |
| 5 | Doors per storey | `challenges/05_doors_per_storey.py` |
| 6 | Delete the basement | `challenges/06_delete_the_basement.py` |

## The model and the wall

- **MiniBIM.ifc**: a residential building, exported from Revit to IFC4 and georeferenced. The same file you took apart with a viewer in BIM A+2.
- **Our wall**: `2pjBMhmIb9UvPqt$wR2ogX`, the façade wall from "Anatomy of an IfcWall". Every question comes back to it.

## Setup

```bash
git clone https://github.com/mlaura1996/BIMAplus3-AI-challenges
cd BIMAplus3-AI-challenges
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux
pip install -r requirements.txt
```

Put `MiniBIM.ifc` in `data/` (see [data/README.md](data/README.md)), then run a question from the `challenges/` folder:

```bash
cd challenges
python 01_how_many_walls.py
```

Tested with Python 3.10 and IfcOpenShell 0.9.0. In Google Colab, run `!pip install ifcopenshell` first.
