# Create Glowing Bacteria

## Overview
This Python script automates the process of inserting a Green Fluorescent Protein (GFP) sequence into a specified site within a plasmid DNA sequence. Utilizing a provided mapping principle, the script also generates the complementary strand for the resulting DNA sequence.

## Features
- **Plasmid and GFP Sequence Handling:** Automatically reads and processes plasmid and GFP sequences from a text file.
- **DNA Site Recognition:** Identifies specific insertion sites within both the plasmid and GFP sequences.
- **GFP Insertion:** Seamlessly inserts the GFP sequence into the plasmid at the designated site.
- **Complementary Strand Generation:** Calculates and outputs the complementary DNA strand for the resulting sequence using a predefined mapping principle.

## How It Works
The script operates by first reading a text file, `plasmid_gfp_example.txt`, which contains:
1. The original plasmid sequence.
2. The designated insertion site on the plasmid.
3. The GFP sequence.
4. The left and right insertion sites on the GFP sequence.

Using this information, it then:
- Finds the exact location to insert the GFP sequence into the plasmid.
- Extracts the portion of the GFP sequence that needs to be inserted.
- Generates the final sequence with the GFP insertion.
- Produces the complementary strand for this new sequence.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/create-glowing-bacteria.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## Usage

1. Prepare a text file named `plasmid_gfp_example.txt` with the following format:
    - Line 1: Original plasmid sequence
    - Line 2: Plasmid insertion site sequence
    - Line 3: GFP sequence
    - Line 4: Left and right GFP insertion site sequences, separated by a space

2. Ensure the text file is in the same directory as the script or provide the path to the file in the script.

3. Run the script (see the [How to Run](#how-to-run) section above).

4. The output will be printed to the console, displaying:
    - The new DNA sequence with the GFP insertion.
    - The complementary strand of the new DNA sequence.

## Example Input and Output

**Input** (in `plasmid_gfp_example.txt`):
```
ATCGTACGATCG
CGA
ATGCGTACGTAGCTAGCG
CGT AGC
```

**Output**:
```
ATCGTACGATCGTAGCTAGCG
TAGCATGCTAGCATCGCA
```

## License

This project is licensed under the [MIT License](LICENSE.txt).
