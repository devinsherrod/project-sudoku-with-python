import clingo
from clingo.application import Application, clingo_main


class SudokuApp(Application):
    def main(self, control, files):
        for file in files:
            control.load(file)

        control.add("base", [], """
            % Each cell gets exactly one number
            1 { sudoku(R,C,N) : N=1..9 } 1 :- R=1..9, C=1..9.

            % No repeated numbers in a row
            :- sudoku(R,C,N), sudoku(R,C2,N), C != C2.

            % No repeated numbers in a column
            :- sudoku(R,C,N), sudoku(R2,C,N), R != R2.

            % No repeated numbers in a 3x3 box
            :- sudoku(R,C,N), sudoku(R2,C2,N),
               (R-1)/3 == (R2-1)/3,
               (C-1)/3 == (C2-1)/3,
               R != R2.

            :- sudoku(R,C,N), sudoku(R2,C2,N),
               (R-1)/3 == (R2-1)/3,
               (C-1)/3 == (C2-1)/3,
               C != C2.

            % Keep the original puzzle numbers
            :- initial(R,C,N), not sudoku(R,C,N).

            #show sudoku/3.
        """)

        control.ground([("base", [])])
        control.solve()


if __name__ == "__main__":
    clingo_main(SudokuApp())

