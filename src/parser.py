def read_file(file_path):
    sequence = ""
    with open(file_path) as fp:
        for line in fp:
            if line[0] != ">":
                sequence += line.strip()

    return sequence