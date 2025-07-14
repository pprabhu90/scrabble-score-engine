# Scrabble Word Scoring Engine

This project includes two Python scripts that compute the highest-scoring Scrabble word from a given set of letters using standard letter scores.

## Features
- Calculates word scores using official Scrabble tile values
- Supports wildcard characters (`*` and `?`)
- Validates words against a reference dictionary (`sowpods.txt`)
- Optimized for readability and teaching purposes

## Files
- `scrabble.py` – input handling, word generation, and scoring logic
- `wordscore.py` – function to calculate the score of a word
- `sowpods.txt` – dictionary of valid Scrabble words (add this file manually)

## How to Run
From the command line:
```bash
python scrabble.py PAINTER
```

## Author
Praj Prabhu