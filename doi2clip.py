import requests
import json
import pyperclip
import sys
import io
from termcolor import colored

# required for converting months from numbers into strings
months = {1: 'jan', 2: 'feb', 3: 'mar', 4: 'apr', 5: 'may', 6: 'jun',
          7: 'jul', 8: 'aug', 9: 'sep', 10: 'oct', 11: 'nov', 12: 'dec'}

# required for defining document type
types = {'journal-article': 'article', 'proceedings-article': 'inproceedings'}

def checkDOI(doi):
    '''Checks whether the provided doi is in the correct format'''
    if doi[:3] == '10.':
        return f'https://doi.org/{doi}'
    elif 'https://doi.org/' in doi:
        return doi
    else:
        print('The provided doi is not correct. Correct formats:\n- https://doi.org/10.XXXXX\n- 10.XXXXX')
        sys.exit()    

def getMetadata(doi):
    '''Download the metadata using requests'''
    doi = checkDOI(doi) # check if the format is correct
    headers = {"Accept": "application/vnd.citationstyles.csl+json"}
    response = requests.get(doi, headers=headers)

    return response.json()

def arrangeAuthors(authors):
    '''Arrange the authors as a single string in the BibTeX format'''
    auth_list = ''
    N = len(authors)

    for i, a in enumerate(authors):
        if i != N-1:
            auth_list += a['family'] + ', ' + a['given'] + ' and '
        else:
            auth_list += a['family'] + ', ' + a['given']

    return auth_list

doi = 'https://doi.org/10.1109/BSN63547.2024.10780647'
metadata = getMetadata(doi)

print(metadata['title'])
# doc_type = types[metadata['type']]
# authors = arrangeAuthors(metadata['author'])
# year = metadata['deposited']['date-parts'][0][0]
# month = months[metadata['deposited']['date-parts'][0][1]]
# # uniqueID is the surname of the first author followed by the publication year
# uniqueID = metadata['author'][0]['family'] + str(year)

# title = metadata['title']
# volume = metadata['volume']
# issn = metadata['ISSN'][-1]
# url = metadata['URL']
# doi_meta = metadata['DOI']
# journal = metadata['container-title']
# publisher = metadata['publisher']
# pages = metadata['page']

# ## \* Initialize Buffer for copying to clipboard */ ##
# original_stdout = sys.stdout
# sys.stdout = io.StringIO()
# ## \* Organize what will be printed */ ##
# if doc_type == 'article':
#   print(f'@{doc_type}{{{uniqueID},')
#   print(f'\t title = {{{title}}},')
#   print(f'\t volume = {{{volume}}},')
#   print(f'\t ISSN = {{{issn}}},')
#   print(f'\t url = {{{url}}},')
#   print(f'\t DOI = {{{doi_meta}}},')
#   print(f'\t journal = {{{journal}}},')
#   print(f'\t publisher = {{{publisher}}},')
#   print(f'\t author = {{{authors}}},')
#   print(f'\t year = {{{year}}},')
#   print(f'\t month = {{{month}}},')
#   print(f'\t pages = {{{pages}}}')
#   print('}')

# # ## \* Get the value from the buffer and reset stdout */ ##
# # captured_output = sys.stdout.getvalue()
# # sys.stdout = original_stdout

# # ## \* Copy the captured output to the clipboard and print it also */ ##
# # pyperclip.copy(captured_output)
# # print(captured_output)
# print(metadata['event'])