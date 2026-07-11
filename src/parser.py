def read_file(file_path):
    sequence = ""
    with open(file_path) as fp:
        for line in fp:
            if line[0] != ">":
                sequence += line.strip()

    return sequence

def scan(base, mutation):
    changes = {}

    for i, _ in enumerate(base):
        if base[i] != mutation[i]:
            changes[i + 1] = {
                "base": base[i],
                "mutation": mutation[i]
            }

    return changes