import sys
from collections import deque


def print_context(filepath: str):
    lines = deque()
    for _ in range(2):
        lines.append("")
    with open(filepath, "r") as f:
        for _ in range(2):
            lines.append(f.readline()[:-1])  # remove newline and add to queue
        line = f.readline()
        while line:
            print(lines[2] + "\t" + "\t".join(lines))
            lines.append(line[:-1])
            lines.popleft()
            line = f.readline()
        for _ in range(2):
            print(lines[2] + "\t" + "\t".join(lines))
            lines.popleft()
            lines.append("")


if __name__ == "__main__":
    print_context(sys.argv[1])
