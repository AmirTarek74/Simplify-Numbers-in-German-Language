# Simplify Numbers, Percentages, and Dates in Text

This Python script simplifies numbers, percentages, and dates in a given german text. It rounds large numbers, replaces percentages with descriptive phrases, and reformats dates into a more readable form. The script leverages regular expressions (regex) for efficient text processing.

## Features:
- Rounds large numbers to the nearest thousand and provides contextual explanations (e.g., millions, thousands).
- Replaces percentages with figurative expressions (e.g., "jeder Vierte" for 25%).
- Reformats dates and years into a more understandable format.
- Flexible input through the command line using `argparse`.

## Solution Overview:
This implementation:
1. Uses regex to match numbers, percentages, and dates within a sentence.
2. Rounds large numbers and provides contextual explanations based on the magnitude.
3. Converts percentages to common phrases like "jeder Vierte" for 25% or "fast alle" for almost 100%.
4. Simplifies date formats, handling both specific days and years.

The program is intended to improve the readability of numeric data in sentences, making it easier to understand for a broader audience.

## Requirements:
- Python 3.x
- No additional libraries are required beyond the Python standard library.

## Setup Instructions:
1. Clone the repository or download the Python script to your local machine.
2. Make sure Python 3.x is installed on your system.

## Usage:

### Running the Script:
To run the script and simplify a sentence from the command line, use the following command:

```bash
python simplify_text.py "Your text goes here."
```
For example:
``` bash
python simplify_text.py "324.620,22 Euro wurden gespendet."
```
### Expected Output:
For the input "324.620,22 Euro wurden gespendet.", the output would be:
``` plaintext
Simplified Text: etwa 325000 Euro wurden gespendet.
```
## Command-Line Arguments:
- sentence: The sentence you want to simplify. This is passed as a string after the script name in the command line.

Feel free to fork this repository, open issues, and submit pull requests. Contributions are welcome to improve functionality or add more features.
