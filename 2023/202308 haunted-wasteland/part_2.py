import utils
from math import gcd


@utils.timeit
def solve(input: str) -> int:
    dir_data, node_data = input.split("\n\n")

    dirs = [0 if char == "L" else 1 for char in dir_data]

    nodes = dict()
    for row in node_data.splitlines():
        key, vals = row.split(" = ")
        nodes[key] = vals[1:-1].split(", ")

    active_nodes_steps = []
    active_nodes = [node for node in nodes if node.endswith("A")]
    for node in active_nodes:
        steps = 0
        while not node.endswith("Z"):
            steps += 1
            node = nodes[node][dirs[0]]
            dirs = dirs[1:] + [dirs[0]]

        active_nodes_steps.append(steps)

    nums = [cycle for cycle in active_nodes_steps]

    lcm = nums.pop()

    for num in nums:
        lcm = lcm * num // gcd(lcm, num)

    return lcm


if __name__ == "__main__":
    with open("2023/202308 haunted-wasteland/input.txt", "r") as file:
        input = file.read()
    print(f"Part 2: {solve(input)}")
