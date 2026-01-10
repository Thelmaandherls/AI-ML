def load_strings(file_name):
    strings = []
    with open(file_name) as f:
        for line in f:
            strings.append(line.rstrip())
    return strings