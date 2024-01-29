import csv
from actions import *
from origin import *
from rights import *

def create_idlist(csv_path):
    id_list = list()
    fhand = open(csv_path, newline='')
    csv_reader = csv.reader(fhand, delimiter=',', quotechar='"')
    for row in csv_reader:
        id_list.append(row[0].strip())
    fhand.close()
    return(id_list)

def generate_header_footer(id):
    premis_header = '''<premis:premis xmlns:premis="http://www.loc.gov/premis/v3" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd" version="3.0">
    <premis:object xsi:type="premis:intellectualEntity">
        <premis:objectIdentifier>
            <premis:objectIdentifierType>system_identifier</premis:objectIdentifierType>
            <premis:objectIdentifierValue>{system_identifier}</premis:objectIdentifierValue>
        </premis:objectIdentifier>
    </premis:object>\n'''.format(system_identifier=id)
    premis_footer = '</premis:premis>'
    return(premis_header, premis_footer)

def disable_all(window, event_type, event_info, date_executed, date_executed_button, executer, role, bd_digit, date_created, date_created_button, creator, rights_basis, date_determ, date_determ_button, terms, rights_notes, determiner):
    window['-CSV_PATH-'].update(disabled=True)
    window['-FILE_BROWSE_BUTTON-'].update(disabled=True)
    window['-OUTPUT-'].update(disabled=True)
    window['-FOLDER_BROWSE_BUTTON-'].update(disabled=True)
    window['-ENCODING-'].update(disabled=True)
    window['-GITHUB-'].update(disabled=True)
    window['-LETS_GOOOO-'].update(disabled=True)
    window['-ABOUT-'].update(disabled=True)
    window['-EXIT-'].update(disabled=True)
    window['-ORIGIN_CB-'].update(disabled=True)
    window['-RIGHTS_CB-'].update(disabled=True)
    window['-ACTION_CB-'].update(disabled=True)
    origin_disable(bd_digit, date_created, date_created_button, creator)
    rights_disable(rights_basis, date_determ, date_determ_button, terms, rights_notes, determiner)
    action_disable(event_type, event_info, date_executed, date_executed_button, executer, role)

def enable_all(values, window, event_type, event_info, date_executed, date_executed_button, executer, role, bd_digit, date_created, date_created_button, creator, rights_basis, date_determ, date_determ_button, terms, rights_notes, determiner):
    window['-CSV_PATH-'].update(disabled=False)
    window['-FILE_BROWSE_BUTTON-'].update(disabled=False)
    window['-OUTPUT-'].update(disabled=False)
    window['-FOLDER_BROWSE_BUTTON-'].update(disabled=False)
    window['-ENCODING-'].update(disabled=False)
    window['-GITHUB-'].update(disabled=False)
    window['-LETS_GOOOO-'].update(disabled=False)
    window['-ABOUT-'].update(disabled=False)
    window['-EXIT-'].update(disabled=False)
    window['-ORIGIN_CB-'].update(disabled=False)
    window['-RIGHTS_CB-'].update(disabled=False)
    window['-ACTION_CB-'].update(disabled=False)
    if values['-ORIGIN_CB-'] == True:
        origin_enable(bd_digit, date_created, date_created_button, creator)
    if values['-RIGHTS_CB-'] == True:
        rights_enable(rights_basis, date_determ, date_determ_button, terms, rights_notes, determiner)
    if values['-ACTION_CB-'] == True:
        action_enable(event_type, event_info, date_executed, date_executed_button, executer, role)