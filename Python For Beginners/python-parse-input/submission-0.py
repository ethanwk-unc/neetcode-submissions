from typing import List

def read_integers() -> List[int]:
    lines = input().split(",")
    for i in range(len(lines)):
        lines[i] = int(lines[i])
    return lines

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
