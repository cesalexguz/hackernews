import json
import sys
import re

"""
    Method that counts the number of words in the title, considering only alphabetic characters

    Args:
        title (str): The title of the article

    Returns:
        int: The number of words in the title
"""
def count_words(title):
    # Remove non-alphabetic characters and split by spaces
    words = re.findall(r'\b\w+\b', title)
    return len(words)


"""
    Method that filters and sorts entries based on the filter type

    Args:
        entries (list): A list of entries to be filtered
        filter_type (str): The type of filter to apply ("less_than_or_equal_to_five_words" or "more_than_five_words")

    Returns:
        list: The filtered and sorted list of entries
"""
def filter_entries(entries, filter_type):
    # If the selected filter is "less or equal than five words, use "points" field to order descending
    if filter_type == "less_than_or_equal_to_five_words":
        filtered = sorted(
            [entry for entry in entries if count_words(entry['title']) <= 5],
            key = lambda x: int(x['points'] or 0),
            reverse = True
        )
    # If the selected filter is "more than five words, use "comments" field to order descending
    elif filter_type == "more_than_five_words":
        filtered = sorted(
            [entry for entry in entries if count_words(entry['title']) > 5],
            key = lambda x: int(x['comments'] or 0),
            reverse = True
        )
    return filtered


if __name__ == "__main__":
    # Read the filter type from command-line arguments
    filter_type = sys.argv[1] if len(sys.argv) > 1 else None

    # Validate the filter type and show an error if it doesn't exist 
    if filter_type not in ["less_than_or_equal_to_five_words", "more_than_five_words"]:
        print("Invalid filter type. Please choose 'less_than_or_equal_to_five_words' or 'more_than_five_words'.")
        sys.exit(1)

    # Load entries from initial data previously saved
    with open('initial-data.json') as f:
        entries = json.load(f)

    # Delete special characters from the title field in each entry
    for entry in entries:
        entry['title'] = entry['title'].replace("\u00e2\u20ac\u201c", "")

    # Filter and sort the entries based on the selected filter
    filtered_entries = filter_entries(entries, filter_type)

    # Save the filtered data in a JSON file with name of the filter
    output_file = f'filtered_{filter_type}.json'
    with open(output_file, 'w') as f:
        json.dump(filtered_entries, f, indent = 4)
