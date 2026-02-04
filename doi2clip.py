import requests
import json
import pyperclip
import sys
import io
import json 

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

def extractInfo(metadata):
    # First extract all common information
    authors = arrangeAuthors(metadata['author'])                                # author names
    pub_date = metadata['published-print']['date-parts'][0]
    year = pub_date[0]                                                          # year of publication
    uniqueID = metadata['author'][0]['family'] + str(year)                      # uniqueID is the surname of the first author followed by the publication year

    if len(pub_date) > 1:
        month = months[pub_date[1]]         # if present, month of publication
    else:
        month = ''

    title = metadata['title']                                                   # main title
    url = metadata['URL']                                                       # url to doi
    doi_meta = metadata['DOI']                                                  # doi without url
    
    ## \* Take cases one-by-one
    if metadata['type'] == 'journal-article':
        doc_type = types[metadata['type']]
        volume = metadata['volume']
        issn = metadata['ISSN'][-1]
        
        journal = metadata['container-title']
        publisher = metadata['publisher']
        pages = metadata['page']

        joined = "".join([f'@{doc_type}{{{uniqueID},\n', f'\t title = {{{title}}},\n', f'\t volume = {{{volume}}},\n', 
            f'\t ISSN = {{{issn}}},\n', f'\t url = {{{url}}},\n', f'\t DOI = {{{doi_meta}}},\n', f'\t journal = {{{journal}}},\n', 
            f'\t publisher = {{{publisher}}},\n', f'\t author = {{{authors}}},\n', 
            f'\t year = {{{year}}},\n', f'\t month = {{{month}}},\n', f'\t pages = {{{pages}}}\n', '}'])

    if metadata['type'] == 'proceedings-article':
        doc_type = types[metadata['type']]
        booktitle = metadata['event']
        publisher = metadata['publisher']
        pages = metadata['page']

        joined = "".join([f'@{doc_type}{{{uniqueID},\n', f'\t title = {{{title}}},\n', f'\t url = {{{url}}},\n',
                          f'\t DOI = {{{doi}}},\n', f'\t booktitle = {{{booktitle}}},\n', f'\t publisher = {{{publisher}}},\n',
                          f'\t author = {{{authors}}},\n', f'\t year = {{{year}}},\n', f'\t month = {{{month}}},\n',
                          f'\t pages = {{{pages}}},\n', '}'])

    return joined


doi = 'https://doi.org/10.1109/BSN63547.2024.10780647'
doi = '10.1109/TNSRE.2025.3594540'
#doi = '10.1109/MeMeA52024.2021.9478688'
metadata = getMetadata(doi)

with open('data.json', 'w') as f:
    json.dump(metadata, f, indent=4)

info = extractInfo(metadata)

## \* Initialize Buffer for copying to clipboard */ ##
original_stdout = sys.stdout
sys.stdout = io.StringIO()

## \* Print information */ ##
print(info)

## \* Get the value from the buffer and reset stdout */ ##
captured_output = sys.stdout.getvalue()
sys.stdout = original_stdout

## \* Copy the captured output to the clipboard and print it also */ ##
pyperclip.copy(captured_output)
print(captured_output)

# Debug lines
#print(len(metadata['published-print']['date-parts'][0]), metadata['published-print']['date-parts'][0])