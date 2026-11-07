from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    
    def __str__(self) -> str:
        s = ""
        for row in range(1, 10):
            if row > 1:
                s += "\n"
                if row == 4 or row == 7:
                    s += "\n"
            for col in range(1, 10):
                if col > 1:
                    if col == 4 or col == 7:
                        s += "  "
                    else:
                        s += " "
                s += str(self.sudoku.get((row, col), "-"))

        return s


    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        for atom in model.symbols(shown=True):
            if atom.name == "sudoku" and len(atom.arguments) == 3:
                row, col, num = [arg.number for arg in atom.arguments]
                sudoku[(row, col)] = num
        return cls(sudoku)
