# Good to be back on the air!
import spacy

# Load the Greek language model in spaCy
nlp = spacy.load('el_core_news_sm')

# First test: print each passage, number by number
file_path = 'matteus_1'

try:
    # Open the file
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        # Read the entire file content
        file.readline() # remove Title
        file_content = file.readline()

        # List of parse symbols (numbers as strings)
        parse_symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
                         "17", "18", "19", "20", "21", "22", "23", "24", "25"]

        # Initialize a list to store passages
        passages = []

        # Split the file content into passages based on parse symbols
        for symbol in parse_symbols:
            parts = file_content.split(symbol, 1)
            file_content = parts[1]
            if len(parts[0]) > 0:
                passages.append(parts[0].strip())
        passages.append(parts[1].strip())

        print("-----------")
        # Print each passage
        for passage in passages:
            print(passage)
            # Process the sentence with spaCy
            doc = nlp(passage)

            # Print tokens and their POS tags and dependencies
            print(f"{'Token':<15} {'POS':<8} {'Dependency':<12} {'Head':<8}")
            print("=" * 50)
            for token in doc:
                print(f"{token.text:<15} {token.pos_:<8} {token.dep_:<12} {token.head.text:<8}")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except IOError:
    print(f"Error: Could not read file '{file_path}'.")
