# Extension Search

This Python script allows you to search for the name of Chrome and Edge extensions by querying the Chrome and Edge web stores. Simply provide a list of extension IDs in a text file, and the script will output their corresponding extension names.

## Requirements

- Python 3
- requests
- requests_html
- bs4

## Usage

To use this script, follow these steps:

1. Create a text file containing the IDs of the extensions you want to search. Each ID should be on a new line.
2. Run the script in the terminal or command prompt, providing the path to the text file as a command line argument. For example: 

   ```python chrome-extension-search.py extensions.txt```

   Note: The script only accepts one argument, which should be the path to the text file.

3. The script will output the extension IDs and names in the following format:
   - If an extension ID is invalid or does not exist, the script will output: 
     ```
     [i] <extension ID> is not a valid Chrome or Edge extension ID.
     ```
   - If an extension ID is valid and its name is found, the script will output:
     ```
     <extension ID> | <extension name>
     ```
   - If an extension ID is valid but its name cannot be found, the script will output:
     ```
     [!] Could not identify <extension ID> | status code - <status code>
     ```
4. The output can be easily copied and pasted into a text editor or document for further analysis.
