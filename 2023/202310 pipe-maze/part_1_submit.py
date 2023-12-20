import aocd.models
import part_1

puzzle = aocd.models.Puzzle(2023, 10)
if not puzzle.answered_a:
    puzzle.answer_a = str(part_1.solve(puzzle.input_data))
