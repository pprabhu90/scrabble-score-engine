import itertools
import string
import sys
from collections import Counter
from wordscore import score_word

def load_words(filename="sowpods.txt"):
    """Load valid Scrabble words into a set for faster lookup."""
    with open(filename, "r") as infile:
        return {word.strip().upper() for word in infile}

def generate_wildcard_variations(word, words):
    """Replace wildcards with all possible letters and return valid words."""
    possible_words = set()
    wildcard_indices = [i for i, letter in enumerate(word) if letter in "*?"]
    
    for replacements in itertools.product(string.ascii_uppercase, repeat=len(wildcard_indices)):
        new_word = list(word)
        for i, replacement in zip(wildcard_indices, replacements):
            new_word[i] = replacement
        new_word = "".join(new_word)
        
        if new_word in words:
            possible_words.add(new_word)
    
    return possible_words

def get_valid_words(rack, words):
    """Generate all valid Scrabble words from the given rack, handling wildcards efficiently."""
    rack = rack.upper()
    wildcards = rack.count("*") + rack.count("?")
    rack_letters = [c for c in rack if c.isalpha()]
    valid_words = set()
    
    word_lengths = {len(word) for word in words}
    
    for length in word_lengths.intersection(range(2, len(rack) + 1)):
        for combination in itertools.permutations(rack, length):
            candidate = "".join(combination)
            
            if "*" in candidate or "?" in candidate:
                valid_words.update(generate_wildcard_variations(candidate, words))
            elif candidate in words:
                valid_words.add(candidate)
    
    return valid_words

def run_scrabble(rack):
    """Find all valid Scrabble words from a given rack and return them with their scores."""
    rack = rack.upper()
    
    if not (2 <= len(rack) <= 7):
        return "Error: The rack must contain between 2 and 7 characters."
    
    if not all(c.isalpha() or c in "*?" for c in rack):
        return "Error: The rack can only contain letters A-Z and at most one '*' and one '?'."
    
    if rack.count("*") > 1 or rack.count("?") > 1:
        return "Error: You can only use up to one '*' and one '?' as wildcards."
    
    words = load_words()
    valid_words = get_valid_words(rack, words)
    
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}
    
    scored_words = [(score_word(word, scores), word) for word in valid_words]
    scored_words.sort(key=lambda x: (-x[0], x[1]))
    
    return scored_words, len(scored_words)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: scrabble.py [RACK]")
        sys.exit(1)
    
    rack = sys.argv[1]
    results, count = run_scrabble(rack)
    for score, word in results:
        print(f"{score} {word}")