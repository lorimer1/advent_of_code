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

