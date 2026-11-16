# AI wrote it. Prove it wrong.

**BIM A+3 · Parametric modelling in BIM · Topic 3: Programming applied to IFC**
Hands-on challenges, 2026/2027

In BIM A+2 you took one IfcWall apart with a viewer. Now you have Python, IfcOpenShell and an AI assistant that writes code in seconds.

Every script in `challenges/` was written by an AI assistant from a short prompt. Every script runs without errors, and every script gives an answer that sounds right. Most of those answers are wrong.

Your job is not to write the code. Your job is to know whether the answer is true.

## The rules

1. **You may use AI.** Use any assistant you like, as much as you like.
2. **Predict before you run.** Write down what you expect the script to print. Then run it.
3. **Find what is wrong.** Compare the output with a second, independent way of getting the same answer.
4. **Fix it.** Change the script so that the answer is right.
5. **Explain it in one sentence.** Why did the AI get it wrong? What did it assume about the file that is not true?
6. **Back every claim with a number.** "It looks fine" is not an answer.

Write your answers in `WORKSHEET.md`. At the end, you will defend one line of your code to us in two minutes.

## The challenges

| # | Challenge | Level | File |
|---|---|---|---|
| 01 | How many walls? | ★ | MiniBIM |
| 02 | Where is our wall? | ★ | MiniBIM |
| 03 | How many metres of wall? | ★★ | MiniBIM |
| 04 | How many 300 mm walls? | ★★ | MiniBIM |
| 05 | Which walls have an opening? | ★★ | MiniBIM |
| 06 | Two scripts, two answers (06a and 06b) | ★★ | MiniBIM |
| 07 | Doors per storey | ★ | MiniBIM |
| 08 | Delete the basement | ★★★ | MiniBIM |
| 09 | The client's rules, in IDS | ★★★ | MiniBIM |
| 10 | Audit an AI-made model | ★★★ | CP1 |

★ warm-up · ★★ core · ★★★ stretch

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux
pip install -r requirements.txt
```

Put the two IFC files in `data/` (see [data/README.md](data/README.md)), then run a challenge from the `challenges/` folder:

```bash
cd challenges
python 01_how_many_walls.py
```

Tested with Python 3.10 and IfcOpenShell 0.9.0. In Google Colab, run `!pip install ifcopenshell ifctester` first.

## The files

- **MiniBIM.ifc**: a ten-storey residential building, exported from Revit to IFC4 and georeferenced. The same file and the same wall (`2pjBMhmIb9UvPqt$wR2ogX`) as in BIM A+2.
- **CP1_AI_model.ifc**: Complexo Pedagógico I at the University of Minho, as an IFC model generated with AI.
