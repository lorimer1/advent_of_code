import aocd.models
import part_2

puzzle = aocd.models.Puzzle(2023, 9)
if not puzzle.answered_b:
    puzzle.answer_b = str(part_2.solve(puzzle.input_data))
