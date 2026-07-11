from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("-b", "--base", help="The file path to the base genome")
    parser.add_argument("-m", "--mutated", help="The file path to the mutated genome")

    args = parser.parse_args()

    if not args.base and not args.mutated:
        print("Base and mutated genomes are required")
        exit(1)
    
    return args

if __name__ == "__main__":
    args = parse_args()

    print(args.base, args.mutated)