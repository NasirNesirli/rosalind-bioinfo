# Rosalind Bioinformatics Solutions

My solutions to problems from [Rosalind](https://rosalind.info), a platform for learning bioinformatics through problem solving.

**Profile:** [nesirli on Rosalind](https://rosalind.info/users/nesirli/)

## Project Structure

```
rosalind-bioinfo/
├── python-village/          # Python programming basics
├── bioinformatics-stronghold/   # Core bioinformatics algorithms
├── bioinformatics-armory/   # Solutions using existing tools
├── textbook-track/          # Companion exercises for textbooks
├── algorithmic-heights/     # Introductory algorithms
├── data/                    # Input data files
├── utils/                   # Shared utility functions
└── main.py                  # Entry point
```

## Tracks

### 🐍 Python Village
If you are completely new to programming, try these initial problems to learn a few basics about the Python programming language. You'll get familiar with the operations needed to start solving bioinformatics challenges in the Stronghold.

### 🧬 Bioinformatics Stronghold
Discover the algorithms underlying a variety of bioinformatics topics: computational mass spectrometry, alignment, dynamic programming, genome assembly, genome rearrangements, phylogeny, probability, string algorithms and others.

### 🛠️ Bioinformatics Armory
Ready-to-use software tools abound for bioinformatics analysis. Whereas in the Stronghold you implement algorithms on your own, in the Armory you solve similar problems by using existing tools.

### 📚 Bioinformatics Textbook Track
A collection of exercises to accompany *Bioinformatics Algorithms: An Active-Learning Approach* by Phillip Compeau & Pavel Pevzner.

### ⛰️ Algorithmic Heights
A collection of exercises in introductory algorithms to accompany *Algorithms*, the popular textbook by Dasgupta, Papadimitriou, and Vazirani.

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for Python package management.

```bash
# Create virtual environment
uv sync

# Activate virtual environment
source .venv/bin/activate

# Run solutions
python bioinformatics-stronghold/dna.py
```

## Requirements

- Python >= 3.13
- uv package manager

## Progress

Track progress and completed problems in each directory.

## Resources

- [Rosalind Homepage](https://rosalind.info)
- [Problem Archive](https://rosalind.info/problems/list-view/)

---

*Solutions are for educational purposes. Always try to solve problems independently first!*
