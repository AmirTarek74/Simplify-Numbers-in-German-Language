import re
import argparse

def simplify_numbers(raw_text):
    """
    Simplifies numbers and percentages in the given text by:
    1. Rounding large numbers to the nearest thousand with "etwa".
    2. Replacing percentages with descriptive phrases.
    3. Adding contextual explanations for large numbers.
    4. Using figurative comparisons for better relatability.
    
    Args:
        raw_text (str): Input text containing numbers, percentages, or dates.
    
    Returns:
        str: Text with simplified and explained numbers.
    """
    
    def round_large_numbers(match):
        """Round large numbers to the nearest thousand and add contextual explanations."""
        number = match.group(0)
        
        number = number.replace('.', '')
        number = number.replace(',', '.')

        rounded = round(float(number))
    
        if rounded >= 1000000:  # Numbers in the millions 
            explanation = "So viel Geld, dass man 100 Autos kaufen konnte"
            return explanation
        
        elif rounded >= 10000 and 'Euro' not in raw_text:  # Numbers in 10 thousands and it's not money
            explanation = "So viele Menschen, wie in ein grobes Fubballstadion passen"
            return explanation
        
        elif rounded >= 1000:  # Numbers in the thousands
            # Round to nearest thousand
            rounded = int(round(rounded, -3))
            explanation = "etwa "+str(rounded)
            return explanation
        return f"etwa {rounded}"

    def simplify_percentages(match):
        """Replace percentages with descriptive and figurative phrases."""
        percentage = float(match.group(1).replace(',', '.'))
        if percentage == 25:
            return "jeder Vierte"
        elif percentage == 50:
            return "die Hälfte"
        elif percentage == 75:
            return "drei von vier"
        elif percentage < 15:
            return "wenige"
        elif percentage < 60:
            return "mehr als ein Drittel"
        elif percentage < 90:
            return "mehr als die Hälfte"
        else:
            return "fast alle"

    # Simplify percentages
    percentage_pattern = r'(\d{1,2}(?:,\d{1,2})?) Prozent'
    raw_text = re.sub(percentage_pattern, simplify_percentages, raw_text)
    
    # Step 1: Skip dates and years
    years_pattern = r'\b(?:Im Jahr|Am|den|der|vom|ab)\s(\d{4})\b'
    raw_text = re.sub(years_pattern, r'YEAR_\1', raw_text)  # Match years with context
    
    date_pattern = r'\b(Am|den|vom|ab)?\s?(\d{1,2})\.\s(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s(\d{4})\b'
    raw_text = re.sub(
        date_pattern, 
        r'DATE_\1_\2_\3_\4', 
        raw_text
    )  

    numbers_pattern = r"\b(?!(YEAR|DATE)_)\b\d{1,3}((.|,)\d{1,3})*(\.\d+,?\d+)?\b"
    # Step 2: Simplify large numbers (exclude placeholders for years and dates)
    raw_text = re.sub(numbers_pattern, round_large_numbers, raw_text)
    
    # Step 4: Restore skipped patterns
    raw_text = re.sub(r'YEAR_(\d{4})', r'Im Jahr \1', raw_text)  # Restore years with full context
    simplified_text = re.sub(
        r'DATE_(Am|den|vom|ab)?_?(\d+)_([\wäöüÄÖÜ]+)_(\d+)', 
        lambda m: f"{m.group(1) + ' ' if m.group(1) else ''}{m.group(2)}. {m.group(3)} {m.group(4)}", 
        raw_text
    )  

    return simplified_text


def main():
    # Set up argparse to handle command-line input
    parser = argparse.ArgumentParser(description='Simplify numbers, percentages, and dates in a text.')
    parser.add_argument('sentence', type=str, help='Input sentence to simplify')
    
    args = parser.parse_args()
    
    # Call the function and print the simplified text
    simplified_text = simplify_numbers(args.sentence)
    print("Simplified Text:", simplified_text)


if __name__ == "__main__":
    main()
