# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        matches = []
        for candidate in possible_anagrams:
            if self.is_anagram(candidate.lower()):
                matches.append(candidate)
        return matches

    def is_anagram(self, candidate):
        if candidate == self.word:
            return False  # Words shouldn't match themselves
        return sorted(candidate) == sorted(self.word)
