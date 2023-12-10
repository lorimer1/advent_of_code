import aocd.models
import part_$n

puzzle = aocd.models.Puzzle($year, $day)
if not puzzle.answered_$x:
    puzzle.answer_$x = str(part_$n.solve(puzzle.input_data))
