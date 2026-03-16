def parse_lines():
    pass

def count_lines_of_code(path, suffixes=None):
    if suffixes is None:
        suffixes = [".py", ".c", ".cpp", ".java", ".js"]

    total = 0

    with open(path, 'r') as fp:
        lines = fp.readlines()
        lines[:] = [line for line in lines if len(line) > 1]
        lines[:] = ["".join(line.split("\n")) for line in lines]
        lines[:] = [line.replace("'", "\"") for line in lines]
        print(len(lines))