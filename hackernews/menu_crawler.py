import subprocess
import os
import json
from datetime import datetime


"""
    Method that executes a console command

    Args:
        command (str): The command to be executed in console
"""
def run_command(command):
    # This method uses subprocess.Popen to run the command and waits for it to complete.
    process = subprocess.Popen(command, shell = True)
    process.communicate()

"""
    Method to delete a file if it exists

    Args:
        file_path (str): The path to the file to be deleted
"""
def delete_file(file_path):
    # This method checks if the file exists and removes it if it does.
    if os.path.exists(file_path):
        os.remove(file_path)

"""
    Method that shows the content of a JSON file in console.

    Args:
        file_path (str): The path to the JSON file 
"""
def show_json(file_path):
    # Confirm if the path exists
    if os.path.exists(file_path):
        # Open the file
        with open(file_path, 'r') as f:
            # Load the data and print it
            data = json.load(f)
            print(json.dumps(data, indent = 4))
    else:
        # Print an error if it does not exist
        print(f"{file_path} does not exist.")

"""
    Method that runs the spider crawler and save the data in a JSON file
"""
def run_crawler():
    # Delete a previous file in case it exists
    delete_file('initial-data.json')
    # Run command in console executing the crawler and save the data in a JSON file
    run_command("scrapy crawl hackernews -o initial-data.json")
    # Print in console the data
    show_json('initial-data.json')
    # Save the action selected in menu in a different JSON file
    store_user_interaction('run_crawler')

"""
    Method that runs the filter function according on the selected filter

    Args:
        filter_type (str): The type of filter to apply ("less_than_or_equal_to_five_words" or "more_than_five_words").
"""
def run_filter(filter_type):
    # Delete a previous file in case it exists
    delete_file(f'filtered_{filter_type}.json')
    # Run command in console executing the python file with filter methods
    run_command(f"python filter_and_store.py {filter_type}")
    # Print in console the data
    show_json(f'filtered_{filter_type}.json')
    # Save the action selected in menu in a different JSON file
    store_user_interaction(filter_type)

"""
    Method that runs the default option which includes running the crawler and both filters.
"""
def run_default():
    # Delete previous files in case they exist
    delete_file('initial-data.json')
    delete_file('filtered_more_than_five_words.json')
    delete_file('filtered_less_than_or_equal_to_five_words.json')
    # Run command in console executing the crawler and save the data in a JSON file
    run_command("scrapy crawl hackernews -o initial-data.json")
    # Run command in console executing the python file with filter methods
    run_command("python filter_and_store.py less_than_or_equal_to_five_words")
    run_command("python filter_and_store.py more_than_five_words")
    # Print in console the initial data and filtered data
    show_json('initial-data.json')
    show_json('filtered_less_than_or_equal_to_five_words.json')
    show_json('filtered_more_than_five_words.json')
    # Save the action selected in menu in a different JSON file
    store_user_interaction('run_default')

"""
    This method stores the user interaction (selected order in menu) and the timestamp in a JSON file

    Args:
        filter_type (str): The filter type selected by user
"""
def store_user_interaction(filter_type):
    # The registry records the timestamp and filter type/order selected by the user in the menu
    user_interaction = {
        'timestamp': datetime.now().isoformat(),
        'filter_type': filter_type
    }

    # Save in file the registry with a line break
    with open('user_interaction.json', 'a') as f:
        json.dump(user_interaction, f)
        f.write('\n')

"""
    Method to show a menu for the user to choose an action.
"""
def menu():
    while True:
        print("\nMenu:")
        print("1. Run crawler")
        print("2. Run 'Less than or equal to five words' filter")
        print("3. Run 'More than five words' filter")
        print("4. Run Default Option 'Execute crawler and both filters'")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            run_crawler()
        elif choice == '2':
            run_filter("less_than_or_equal_to_five_words")
        elif choice == '3':
            run_filter("more_than_five_words")
        elif choice == '4':
            run_default()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()