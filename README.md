# Bioinformatics Software Testing

## Overview

This project demonstrates unit testing and error handling
for Python functions working with peptide sequences.

The main component is `peptide.py`, which provides functions
for validating and manipulating peptide sequences.

## Core functionality

### Peptide concatenation

`concatenacion_peptidos()` validates two peptide sequences
and returns their concatenation.

### Poly-H generation

`polyh()` validates a peptide sequence and generates a
sequence with a specified number of histidine residues.

## Testing

The functionality is tested using Python's `unittest`
framework.

Tests cover:

- Valid peptide sequences
- Invalid amino-acid codes
- Peptide concatenation
- Poly-H generation
- Error handling

## Project structure

src/

└── peptide.py

tests/

└── test_peptide.py
