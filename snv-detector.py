from argparse import ArgumentParser

from src import parser

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("-b", "--base", required=True, help="The file path to the base genome")
    parser.add_argument("-m", "--mutated", required=True, help="The file path to the mutated genome")

    args = parser.parse_args()
    
    return args

if __name__ == "__main__":
    args = parse_args()

    base_sequence = parser.read_file(args.base)
    mutated_sequence = parser.read_file(args.mutated)

    if len(base_sequence) != len(mutated_sequence):
        print("Sequence lenghts do not match!")
        exit(1)

    scan_results = parser.scan(base_sequence, mutated_sequence)

    print(f"{'Position':<10}{'Ref':<6}{'Mut':<6}")
    print("-" * 22)
    for pos, change in scan_results.items():
        print(f"{pos:<10}{change['base']:<6}{change['mutation']:<6}")