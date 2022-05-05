"""Boyer-Moore string-search algorithm"""
from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    """Returns the bad characters table based on pattern"""
    table = dict()
    pattern_length = len(pattern)
    for index in range(0, pattern_length):
        # key will be a character, value = Max(1,Length of Pattern - Index -1)
        table[pattern[index]] = max(1, pattern_length - index - 1)
    return table


class Bm(object):
    """
    A class to represent Boyer-Moore string-search algorithm.

    Attributes
    ----------
    text : str
        A string where to search
    pattern : str
        A string that will be searched
    table: Dict[str, int]
        It is a bad characters' table that will be used to decide slide width

    Methods
    -------
    decide_slide_width(c: str) -> int
        Return shift value based on bad characters 'table' of the given string 'c'
    search() -> int:
        Return the first occurrence index from 'text' based on given 'pattern'
    """

    def __init__(self, text: str, pattern: str):
        """
        Constructs all the necessary attributes for the Boyer-Moore algorithm object

        Parameters
        ----------
        text : str
            A text where to search
        pattern : str
            A text that will be searched
        table: Dict[str, int]
            It is a bad character table that will be used to decide slide width
        """

        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        """Return slide width value of the given string 'c' by using bad character table"""

        assert len(c) == 1
        return self.table.get(c, len(self.pattern))

    def search(self) -> int:
        """
        Apply Boyer-Moore string search algorithm to find pattern in text
        that uses bad character table.

        Returns
        -------
        First occurrence index of the pattern from 'text'.
        And if the pattern does not exist, then it will return -1.
        """

        text_length = len(self.text)
        pattern_length = len(self.pattern)
        i = pattern_length - 1
        while i < text_length:
            match = True

            for j in range(pattern_length):
                if self.text[i - j] != self.pattern[-1 - j]:
                    match = False
                    break

            if match:
                return i - pattern_length + 1
            i += self.decide_slide_width(self.text[i])
        return -1
