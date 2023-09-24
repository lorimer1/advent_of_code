## 01 Not Quite Lisp
```python
    from itertools import accumulate
    travel = lambda acc, c: acc + (1 if c == "(" else -1)
    floors_visited = list(accumulate(data, travel, initial=0))
    return next(i for i, floor in enumerate(floors_visited) if floor < 0)
```

## 02 I Was Told There Would Be No Math
```python
    from itertools import starmap
    paper = lambda a, b, c: 3 * a * b + 2 * b * c + 2 * c * a
    return sum(starmap(paper, data))
```

## 03 Perfectly Spherical Houses in a Vacuum
```python
    directions = {"^": -1j, "v": +1j, "<": -1, ">": 1}
    locations[i % players] += directions[d]
    visited |= {locations[i % players]}
```

## 04 The Ideal Stocking Stuffer
```python
    from hashlib import md5
    from itertools import count
    for i in count(start)
```

## 05 Doesn't He Have Intern-Elves For This?
```python
    sum(c in "aeiou" for c in s) >= 3
    any(a == b for a, b in zip(s, s[1:]))
    all(f not in s for f in ("ab", "cd", "pq", "xy"))
```

## 06 Probably a Fire Hazard
```python
    from collections import namedtuple
    Statement = namedtuple("Statement", ["action", "start_x", "start_y", "end_x", "end_y"])
    start_x, start_y = map(int, parts[2].split(","))
    statement_obj = Statement(action, start_x, start_y, end_x, end_y)
```

## 07 Some Assembly Required
```python
    from functools import lru_cache
    from operator import and_, or_, lshift, rshift
    gates = {"AND": and_, "OR": or_, "LSHIFT": lshift, "RSHIFT": rshift}
    @lru_cache
    def get_wire_value(wire):
        try:
            return int(wire)
        except ValueError:
            gate_config = wires[wire]
            if len(gate_config) == 1:
                return get_wire_value(gate_config[0])
            elif len(gate_config) == 2:
                return ~get_wire_value(gate_config[1]) & 0xFFFF
            else:
                gate = gates[gate_config[1]]
                return gate(
                    get_wire_value(gate_config[0]), get_wire_value(gate_config[2])
                )

    return get_wire_value(wire)        
```

## 08 Matchsticks
```python
    return sum(len(line) - len(eval(line)) for line in data)
    return sum(line.count(r'"') + line.count("\\") + 2 for line in data)
```

## 09 All in a Single Night
```python
    from itertools import permutations

    def parse_line(line):
        a, _, b, _, dist = line.split()
        return a, b, int(dist)

    def parse(puzzle_input: str) -> list:
        data = [parse_line(line) for line in puzzle_input.splitlines()]
        return data

    def create_relations(data):
        locations = set()
        relations = dict()
        for a, b, dist in data:
            locations |= {a, b}
            relations[(a, b)] = dist
            relations[(b, a)] = dist
        return locations, relations

    def solve(puzzle_input: str, func):
        data = parse(puzzle_input)
        locations, relations = create_relations(data)
        totals = []
        for route in permutations(locations):
            this_total = 0
            for trip in zip(route, route[1:]):
                this_total += relations[trip]
            totals.append(this_total)

        return func(totals)
```

## 10 Elves Look, Elves Say
```python
    data = list(map(int, puzzle_input))
```

## 11 Corporate Policy
```python
    has_increasing_straight = lambda pw_nums: (
        any(a == b - 1 == c - 2 for a, b, c in zip(pw_nums, pw_nums[1:], pw_nums[2:]))
    )
    has_increasing_straight(list(map(ord, password)))
```

## 12 JSAbacusFramework.io
```python
    numbers = re.compile("-?\d+")
    data = list(map(int, re.findall(numbers, puzzle_input)))
    jason = json.loads(puzzle_input)
    def find_sum(jason: list) -> int:
        if type(jason) is int:
            return jason

        if type(jason) is dict:
            if "red" in jason.values():
                return 0
            else:
                return sum(map(find_sum, jason.values()))

        if type(jason) is list:
            return sum(map(find_sum, jason))
        else:
            return 0    
```

## 13 Knights of the Dinner Table
```python
    for this_perm in itertools.permutations(persons):
        clockwise = list(this_perm)
        clockwise.append(
            clockwise[0]
        )  # last person is sitting next to first (circular table)   
```

## 14 Reindeer Olympics
```python
    cycles, remaining_sec = divmod(sec, deer.on_time + deer.off_time)
    deer_distances = {deer.name: distance(deer, sec) for deer in data}
```

## 15 Science for Hungry People
```python
    for sugar in range(100):
        for sprinkles in range(100 - sugar):
            for candy in range(100 - sugar - sprinkles):
                chocolate = 100 - sugar - sprinkles - candy
```

## 16 Aunt Sue
```python
    name_part_len = len(line.split(": ")[0])
    sue_part, rest = line[:name_part_len], line[name_part_len + 2 :]
```

## 17 No Such Thing as Too Much
```python
    from itertools import combinations
    combos = (com for sub in range(len(data)) for com in combinations(data, sub + 1))
```

## 18 Like a GIF For Your Yard
```python 
    import copy
    new_grid = copy.deepcopy(grid)
```

## 19 Medicine for Rudolph

## 20 Infinite Elves and Infinite Houses

## 21 RPG Simulator 20XX

## 22 Wizard Simulator 20XX

## 23 Opening the Turing Lock

## 24 It Hangs in the Balance
```python
from functools import reduce
from operator import mul
qes = [
    reduce(mul, c) for c in combinations(all_weights, i) if sum(c) == goal_weight
]
```