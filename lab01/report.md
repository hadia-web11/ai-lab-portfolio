[Uploading Lab01_Report.pdf…]()
# Lab 01 Report - Environment Setup, Jupyter and Git
Date: 23 Oct 2026

## 1. Installation evidence
```
conda create -n ai-lab python=3.11 -y
conda activate ai-lab
pip install ipykernel
python -m ipykernel install --user --name ai-lab --display-name "Python (ai-lab)"
```
<img width="1364" height="651" alt="image" src="https://github.com/user-attachments/assets/d7fd0ec3-e626-42a9-8b57-279bccc52991" />

[Uploading lab01_setup.html…]()
[Uploading Lab01_Report.pdf…]()

## 2. Inspection outputs
See `inspect_reports.txt` (Titanic and Penguins datasets, produced by `inspect.py`) and `lab01_setup.ipynb`.

- Missing values (Titanic, seaborn version): deck 688, age 177, embarked 2, embark_town 2.
- Largest std/mean ratio: sibsp and parch (about 2.1), then fare (about 1.5).
  Unscaled columns with large spread dominate distance- and gradient-based models, so scaling is needed.

## 3. Git graph
Paste the output of this command run in your repo:
## 3. Git graph

Output of `git log --oneline --graph --all`:

* 62c65b0 (HEAD -> main, origin/main) Add exercise 3 note
* be245f3 Add exercise 2 note
* b6d6336 Add exercise 1 note
* bd103d0 Lab 01: environment setup and first notebook
```
git log --oneline --graph --all
```

## 4. Home assignment
`inspect.py` defines `inspect(path_or_url)` and was run on two public datasets (Titanic, Penguins).
