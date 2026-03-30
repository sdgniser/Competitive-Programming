# Competitive-Programming

Discord server for discussions and chatting: https://discord.gg/w2bSsQkBTe


Welcome! 
Each day, new problems are posted, submit your solutions with explanations.

This guide explains the structure and how to submit your work.

## Directory Structure

Your repo should look like this:

```
Competitive-Programming/
├── Day-01--23-03-2026/
│   ├── questions.md              # Posted by maintainer
│   ├── editorial.md              # Concepts & resources
│   ├── DSV_Vinay-solutions/
│   │   ├── problem1.py           # Your solution
│   │   ├── problem1.md           # Explanation 
│   │   ├── problem2.cpp          # Your solution
│   │   └── problem2.md           # Explanation
│   ├── Hari(unc)-solutions/
│   │   ├── problem1.py
│   │   ├── problem1.md
│
├── Day-02--24-03-2026/
│   ├── questions.md
│   ├── editorial.md
│   ├── DSV_Vinay-solutions/
│   │   ├── problem1.py
│   │   ├── problem1.md
│   │   └── problem2.py
│   └── Hari(unc)-solutions/
│       ├── problem1.cpp
│       ├── problem1.md
│
└── README.md

```

---

## How to Submit 

Setup your local repos  connections to GitHub:
All these terms are just names for repos (These names follow the standard convention)
- **`origin`** = your fork (the copy under YOUR account)
  - You push code here: `git push origin main`
  - This is where your work lives in isolation

- **`upstream`** = the original repo (the club's repo)
  - You pull questions from here: `git pull upstream main`
  - The maintainer posts daily questions to `upstream/main`
  - You stay in sync with the latest problems by pulling from this repo.

`upstream` is the latest news for problems. `origin` is your workspace.

---

### Step 1: Fork the Repository
Go to GitHub and fork this repository to your own account. This creates your own copy where you can push code.

### Step 2: Clone Your Fork
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Competitive-Programming.git
cd Competitive-Programming
```
This creates a local copy of YOUR fork on your device ( called a clone)

### Step 3: Add Upstream Remote
This links your clone to the original repo, so you can pull daily questions conviniently:

```bash
git remote add upstream https://github.com/sdgniser/Competitive-Programming.git
```

**Verify your remotes:**
```bash
git remote -v
# origin    → your fork (where you push)
# upstream  → club's repo (where you pull questions from)
```

### Step 4: Sync with Daily Questions
Each morning (or before starting), pull the latest questions from the club repo's `main` branch:

```bash
git pull upstream main
```

This ensures you have the newest `Day-XX` folder with today's problems.

### Step 5: Find Today's Day Folder & Create Your Solutions Directory
Look for the folder matching today's date: `Day-XX--DD-MM-YYYY`

Example: `Day-01--30-03-2026`

Inside that day folder, create a directory with your username:

```bash
mkdir Day-01--23-03-2026/YOUR_USERNAME-solutions
cd Day-01--23-03-2026/YOUR_USERNAME-solutions
```

### Step 6: Add Your Code
Create files named `problem1.py`, `problem2.cpp`, etc. (matching the language you used).

For each solution, you **must** also add a `problem1.md`, `problem2.md` file with your approach.

```
Day-01--23-03-2026/
└── YOUR_USERNAME-solutions/
    ├── problem1.py
    ├── problem1.md          
    ├── problem2.cpp
    └── problem2.md          
```

### Step 7: Commit & Push
```bash
git add Day-01--23-03-2026/YOUR_USERNAME-solutions/
git commit -m "Day-01: Add solutions for problems 1-2"
git push origin main
```

### Step 8: Open a Pull Request
Go to your fork on GitHub. You'll see a prompt to open a PR. Click it and submit a PR from your fork's `main` branch to the original repo's `main` branch.

The maintainer will review and merge your solutions, so they appear in the repository immediately.

---

## Daily Workflow Quick Reference

Each day, follow these steps:

```bash
# 1. Sync with latest questions
git pull upstream main

# 2. Create/navigate to today's solutions directory
cd Day-XX--DD-MM-YYYY/YOUR_USERNAME-solutions

# 3. Write your solutions (problem1.py, problem2.cpp, etc.)
# 4. Write explanations (problem1.md, problem2.md, etc.)

# 5. Commit and push
git add .
git commit -m "Day-XX: Add solutions"
git push origin main

# 6. Open a PR on GitHub (or push to your existing PR)
```


## File Naming Convention

| Type | Format | Example |
|------|--------|---------|
| **Source Code** | `problem[n].[ext]` | `problem1.py`, `problem2.cpp`, `problem3.java` |
| **Explanation** | `problem[n].md` | `problem1.md` (approach, complexity, edge cases) |

---

## Example: Full Submission

**Username:** `DSV_Vinay`  
**Date:** March 23rd, 2026  
**Problems:** Solved problems 1 & 2 in Python

```
Day-XY--23-03-2026/
└── DSV_Vinay-solutions/
    ├── problem1.py          # Your solution code
    ├── problem1.md          # Required: approach explanation
    ├── problem2.py
    └── problem2.md          # Required: approach explanation
```

**problem1.py**
```python
# Your solution here
```

**problem1.md** 
```markdown
## [Problem Title]

### Approach
- Observation: ...
- Strategy: ...

whatever else you want to add such as comments and doubts.
```

---

## Questions?
Go to the **#dailies-submission-help** on our discord server in the Competitive Programming category.
