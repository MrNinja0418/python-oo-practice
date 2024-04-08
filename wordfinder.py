"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ...

import random

class WordFinder:
    """Find and provide random words from a file."""

    def __init__(self, Users\Jason Gutwein\Coding_2\python-oo-practice\words.txt):
        """Initialize with a path to a file containing words."""
        self.filepath = filepath
        self.words = self.read_words_from_file()
        print(f"{len(self.words)} words read")

    def read_words_from_file(self):
        """Read words from the file."""
        with open(self.filepath, 'r') as file:
            return [word.strip() for word in file.readlines() if word.strip()]

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Find and provide random words from a file with special requirements."""

    def read_words_from_file(self):
        """Read words from the file, excluding blank lines and comments."""
        with open(self.filepath, 'r') as file:
            return [word.strip() for word in file.readlines() if word.strip() and not word.startswith("#")]


# Testing the classes
if __name__ == "__main__":
    # Testing WordFinder
    print("Testing WordFinder:")
    wf = WordFinder("words.txt")
    print(wf.random())
    print(wf.random())
    print(wf.random())

    # Testing SpecialWordFinder
    print("\nTesting SpecialWordFinder:")
    swf = SpecialWordFinder("special_words.txt")
    print(swf.random())
    print(swf.random())
    print(swf.random())
