import utils


@utils.timeit
def solve(input: str) -> int:
    dir_data, node_data = input.split("\n\n")

    dirs = [0 if char == "L" else 1 for char in dir_data]

    nodes = dict()
    for row in node_data.splitlines():
        key, vals = row.split(" = ")
        nodes[key] = vals[1:-1].split(", ")

    node = "AAA"
    steps = 0
    while node != "ZZZ":
        steps += 1
        node = nodes[node][dirs[0]]
        dirs = dirs[1:] + [dirs[0]]
    return steps


if __name__ == "__main__":
    with open("2023/202308 haunted-wasteland/input.txt", "r") as file:
        input = file.read()
    print(f"Part 1: {solve(input)}")
