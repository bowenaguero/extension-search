import argparse
from requests_html import HTMLSession
from bs4 import BeautifulSoup

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def validate_chrome_extension_id(extension_id):
    if len(extension_id) != 32:
        return False

    for char in extension_id:
        if not char.isalnum() and char != '_':
            return False

    return True

parser = argparse.ArgumentParser(description='Search a list of chrome extensions...')
parser.add_argument("file", help='text file containing extenions IDs to search')

args = parser.parse_args()

extensionsfile = args.file
extensions = {}

url = 'https://microsoftedge.microsoft.com/addons/detail/'
session = HTMLSession()

with open (extensionsfile, 'r') as f:
    for line in f:
        ext = line.strip()
        if validate_chrome_extension_id(ext):
            extensions[ext] = {'status' : '', 'found': False, 'value' : 'NA'}
        else:
            print(f"{bcolors.WARNING}[i]{bcolors.ENDC} {ext} is not a valid edge extension ID.")
            continue

for ext in list(extensions):
    try:
        response = session.get(f"{url}{ext}")
        response.html.render()
        html_content = response.html.html
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.title.string

        extensions[ext]['status'] = response.status_code
        
        if len(title) > 22:
            extensions[ext]['found'] = True
            extensions[ext]['value'] = title
            print(f'{bcolors.OKGREEN}{ext}{bcolors.ENDC} | {title}')
    
    except Exception as e:
        print(e)

print()
for ext, info in extensions.items():
    if not info['found']:
        print(f"{bcolors.FAIL}[!]{bcolors.ENDC} Could not identify {ext} | status code - {extensions[ext]['status']}")
