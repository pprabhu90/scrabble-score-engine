"""
This module provides a function to calculate the Scrabble score of a word.
"""


def score_word(word, scores):
    """Calculate the Scrabble score of a word based on the given scores dictionary."""
    return sum(scores.get(letter.lower(), 0) for letter in word)
