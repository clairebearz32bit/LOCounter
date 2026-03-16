def parse_lines():
    pass

def count_lines(path, suffixes=None):
    if suffixes is None:
        suffixes = [".py", ".c", ".cpp", ".java", ".js"]

    total = 0

    with open(path, 'r') as fp:
        lines = fp.readline()
        print(type(lines))
        print(lines)