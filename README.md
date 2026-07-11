<h1 align="center">🧬 SNV-Detector</h1>

<p align="center">
    A command-line utility to detect single nucleotide variants (SNVs) between a base and mutated genome sequence.
</p>

<p align="center">
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
</p>

A modular, zero-dependency Python CLI built to compare two aligned genomic sequences. It reads raw FASTA-style input for a base and a mutated genome, scans them position by position, and reports every mismatched base as a single nucleotide variant.

## Install

Clone the repository directly:
```bash
git clone https://github.com/eben-vranken/snv-detector.git
cd snv-detector
```

## Usage

Pass a base genome file and a mutated genome file. The tool compares the two sequences and reports every position where they differ.

```bash
python snv-detector.py --base data/synthetic_zika.fasta --mutated data/synthetic_zika_mutated.fasta
```

### Short Flags

The same arguments are available in short form:

```bash
python snv-detector.py -b data/synthetic_zika.fasta -m data/synthetic_zika_mutated.fasta
```

### Example Output

```
Position  Ref   Mut
----------------------
9         A     G
34        G     T
...
```

## Configuration Matrix

| Argument | Option / Choices | Default | Description |
| --- | --- | --- | --- |
| `-b`, `--base` | *Path string* | *Required* | Path to the FASTA file containing the base (reference) genome. |
| `-m`, `--mutated` | *Path string* | *Required* | Path to the FASTA file containing the mutated genome. |

## Feature Set

* **FASTA-Aware Parsing:** Strips header lines and stray whitespace from both input files before scanning.
* **Position-by-Position Scanning:** Walks the base and mutated sequences in lockstep to find every mismatched base.
* **SNV Reporting:** Reports each variant's 1-based position, reference base, and mutated base in a clean tabular format.
* **Length Validation:** Exits with an error if the base and mutated sequences are not the same length.

## License

MIT