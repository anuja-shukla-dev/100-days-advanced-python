def read_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line


lines = read_lines("Day-18-Generators-and-yield/sample.txt")

for line in lines:
    print(line)