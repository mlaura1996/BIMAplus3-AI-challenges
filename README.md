# One model, six questions

**BIM A+3 · Parametric modelling in BIM · Topic 3: Programming applied to IFC**
Hands-on challenges, 2026/2027

One building, one wall, six questions. For each question you get a request and a Python script written for it.

## Goals

- Explore the repository and its code.
- For each challenge, try to execute the code.
- Check if the code is doing what it is intended to do.
- Answer the questions.

## Report

The review of the code and the answers to the questions must be delivered in a report. Include images of the outputs and the IFC documentation to explain your line of argument.

## The questions

| # | Question | Script |
|---|---|---|
| 1 | How many walls? | `challenges/01_how_many_walls.py` |
| 2 | Where is our wall? | `challenges/02_where_is_the_wall.py` |
| 3 | How many walls like ours? | `challenges/04_300mm_walls.py` |
| 4 | Which walls have an opening? | `challenges/05_walls_with_openings.py` |
| 5 | Doors per storey | `challenges/07_doors_per_storey.py` |
| 6 | Delete the basement | `challenges/08_delete_the_basement.py` |

## The model and the wall

- **MiniBIM.ifc**: a residential building, exported from Revit to IFC4 and georeferenced. The same file you took apart with a viewer in BIM A+2.
- **Our wall**: `2pjBMhmIb9UvPqt$wR2ogX`, the façade wall from "Anatomy of an IfcWall".

## Setup

Clone the repository with git, or with GitHub Desktop (File → Clone repository → URL):

```bash
git clone https://github.com/mlaura1996/BIMAplus3-AI-challenges
cd BIMAplus3-AI-challenges
pip install -r requirements.txt
```

Put `MiniBIM.ifc` in `data/` (see [data/README.md](data/README.md)), then run a question from the `challenges/` folder:

```bash
cd challenges
python 01_how_many_walls.py
```

Tested with Python 3.10 and IfcOpenShell 0.9.0. In Google Colab, run `!pip install ifcopenshell` first.
