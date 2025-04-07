import unittest
from sudoku import SudokuSolver

class TestSudokuSolver(unittest.TestCase):

    def test_valid_sudoku_1(self):
        sudoku = [
            5, 3, 0, 0, 7, 0, 0, 0, 0,
            6, 0, 0, 1, 9, 5, 0, 0, 0,
            0, 9, 8, 0, 0, 0, 0, 6, 0,
            8, 0, 0, 0, 6, 0, 0, 0, 3,
            4, 0, 0, 8, 0, 3, 0, 0, 1,
            7, 0, 0, 0, 2, 0, 0, 0, 6,
            0, 6, 0, 0, 0, 0, 2, 8, 0,
            0, 0, 0, 4, 1, 9, 0, 0, 5,
            0, 0, 0, 0, 8, 0, 0, 7, 9
        ]

        expected_solution = [
            5, 3, 4, 6, 7, 8, 9, 1, 2,
            6, 7, 2, 1, 9, 5, 3, 4, 8,
            1, 9, 8, 3, 4, 2, 5, 6, 7,
            8, 5, 9, 7, 6, 1, 4, 2, 3,
            4, 2, 6, 8, 5, 3, 7, 9, 1,
            7, 1, 3, 9, 2, 4, 8, 5, 6,
            9, 6, 1, 5, 3, 7, 2, 8, 4,
            2, 8, 7, 4, 1, 9, 6, 3, 5,
            3, 4, 5, 2, 8, 6, 1, 7, 9
        ]

        solver = SudokuSolver(sudoku)
        solution = solver.get_solution()
        self.assertEqual(solution, expected_solution)

    def test_valid_sudoku_2(self):
        sudoku = [
            5, 0, 6, 0, 0, 7, 0, 1, 9,
            3, 0, 4, 0, 1, 0, 0, 8, 0,
            1, 0, 9, 6, 0, 0, 0, 5, 0,
            6, 0, 8, 0, 3, 0, 9, 0, 4,
            7, 0, 0, 5, 9, 8, 0, 6, 0,
            0, 0, 0, 7, 0, 0, 0, 0, 5,
            0, 0, 0, 8, 0, 0, 5, 0, 3,
            8, 0, 5, 3, 4, 9, 6, 2, 0,
            4, 0, 0, 2, 0, 0, 0, 9, 0
        ]

        expected_solution = [
            5, 8, 6, 4, 2, 7, 3, 1, 9,
            3, 2, 4, 9, 1, 5, 7, 8, 6,
            1, 7, 9, 6, 8, 3, 4, 5, 2,
            6, 5, 8, 1, 3, 2, 9, 7, 4,
            7, 4, 3, 5, 9, 8, 2, 6, 1,
            2, 9, 1, 7, 6, 4, 8, 3, 5,
            9, 6, 2, 8, 7, 1, 5, 4, 3,
            8, 1, 5, 3, 4, 9, 6, 2, 7,
            4, 3, 7, 2, 5, 6, 1, 9, 8
        ]

        solver = SudokuSolver(sudoku)
        solution = solver.get_solution()
        self.assertEqual(solution, expected_solution)

    def test_valid_sudoku_3(self):
        sudoku = [
            0, 9, 0, 0, 7, 0, 0, 0, 1,
            5, 2, 0, 8, 0, 0, 6, 4, 0,
            1, 0, 0, 5, 0, 0, 0, 0, 0,
            0, 3, 0, 0, 1, 0, 0, 0, 2,
            6, 0, 1, 0, 2, 0, 0, 7, 0,
            0, 4, 9, 0, 0, 0, 0, 8, 5,
            0, 8, 0, 0, 5, 0, 4, 0, 6,
            0, 0, 0, 2, 0, 4, 7, 0, 0,
            0, 0, 0, 0, 0, 6, 0, 1, 0,
        ]

        expected_solution = [
            8, 9, 4, 6, 7, 2, 5, 3, 1,
            5, 2, 7, 8, 3, 1, 6, 4, 9,
            1, 6, 3, 5, 4, 9, 8, 2, 7,
            7, 3, 8, 4, 1, 5, 9, 6, 2,
            6, 5, 1, 9, 2, 8, 3, 7, 4,
            2, 4, 9, 7, 6, 3, 1, 8, 5,
            3, 8, 2, 1, 5, 7, 4, 9, 6,
            9, 1, 6, 2, 8, 4, 7, 5, 3,
            4, 7, 5, 3, 9, 6, 2, 1, 8,
        ]

        solver = SudokuSolver(sudoku)
        solution = solver.get_solution()
        self.assertEqual(solution, expected_solution)

    def test_valid_sudoku_4(self):
        sudoku = [
            0, 0, 0, 0, 8, 0, 9, 0, 3,
            0, 1, 5, 4, 2, 0, 6, 0, 7,
            0, 0, 0, 0, 7, 1, 2, 0, 4,
            0, 4, 9, 5, 0, 8, 0, 0, 0,
            0, 7, 0, 2, 6, 0, 0, 0, 0,
            2, 0, 0, 0, 3, 0, 0, 9, 0,
            1, 3, 0, 0, 0, 6, 4, 0, 0,
            7, 6, 0, 1, 9, 0, 5, 0, 8,
            5, 0, 8, 3, 0, 0, 1, 0, 2,
        ]

        expected_solution = [
            4, 2, 7, 6, 8, 5, 9, 1, 3,
            9, 1, 5, 4, 2, 3, 6, 8, 7,
            6, 8, 3, 9, 7, 1, 2, 5, 4,
            3, 4, 9, 5, 1, 8, 7, 2, 6,
            8, 7, 1, 2, 6, 9, 3, 4, 5,
            2, 5, 6, 7, 3, 4, 8, 9, 1,
            1, 3, 2, 8, 5, 6, 4, 7, 9,
            7, 6, 4, 1, 9, 2, 5, 3, 8,
            5, 9, 8, 3, 4, 7, 1, 6, 2,
        ]

        solver = SudokuSolver(sudoku)
        solution = solver.get_solution()
        self.assertEqual(solution, expected_solution)

    def test_invalid_board_length(self):
        self.assertRaises(ValueError, SudokuSolver, [1, 2, 3])

    def test_unsolvable_sudoku(self):
        unsolvable = [
			5, 1, 6, 8, 4, 9, 7, 3, 2,
			3, 0, 7, 6, 0, 5, 0, 0, 0,
			8, 0, 9, 7, 0, 0, 0, 6, 5,
			1, 3, 5, 0, 6, 0, 9, 0, 7,
			4, 7, 2, 5, 9, 1, 0, 0, 6,
			9, 6, 8, 3, 7, 0, 0, 5, 0,
			2, 5, 3, 1, 8, 6, 0, 7, 4,
			6, 8, 4, 2, 0, 7, 5, 0, 0,
			7, 9, 1, 0, 5, 0, 6, 0, 8
		]
        solver = SudokuSolver(unsolvable)
        solution = solver.get_solution()
        self.assertIsNone(solution)

    if __name__ == '__main__':
        unittest.main()
