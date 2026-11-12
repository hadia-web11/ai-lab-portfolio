# Lab 01 Report - Environment Setup, Jupyter and Git
Date: 23 Oct 2026

## 1. Installation evidence
```
conda create -n ai-lab python=3.11 -y
conda activate ai-lab
pip install ipykernel
python -m ipykernel install --user --name ai-lab --display-name "Python (ai-lab)"
```
(Add your screenshot of the kernel "Python (ai-lab)" selected in a notebook here.)

## 2. Inspection outputs
See `inspect_reports.txt` (Titanic and Penguins datasets, produced by `inspect.py`) and `lab01_setup.ipynb`.

- Missing values (Titanic, seaborn version): deck 688, age 177, embarked 2, embark_town 2.
- Largest std/mean ratio: sibsp and parch (about 2.1), then fare (about 1.5).
  Unscaled columns with large spread dominate distance- and gradient-based models, so scaling is needed.

## 3. Git graph
Paste the output of this command run in your repo:
```
git log --oneline --graph --all
```

## 4. Home assignment
`inspect.py` defines `inspect(path_or_url)` and was run on two public datasets (Titanic, Penguins).
