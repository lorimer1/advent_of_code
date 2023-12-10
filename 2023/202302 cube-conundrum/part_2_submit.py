import aocd.models
import part_2

puzzle = aocd.models.Puzzle(2023, 1)
if not puzzle.answered_a:
    puzzle.answer_a = str(part_2.solve(puzzle.input_data))
