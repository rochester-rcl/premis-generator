import PySimpleGUI as sg
import os
import json
import xmltodict
import webbrowser
from icon import *
from core import *
from origin import *
from rights import *
from actions import *

vsc_theme = {'BACKGROUND': '#252525',
            'TEXT': '#7edcf0',
            'INPUT': '#181818',
            'TEXT_INPUT': '#5dd495',
            'SCROLL': '#252525',
            'BUTTON': ('#dcdca1', '#181818'),
            'PROGRESS': ('#dcdca1', '#181818'),
            'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

alt_background = '#181818'
medium_font = 'Courier 12 bold'
big_font = 'Courier 14 bold'
program_icon = icon()
sg.set_options(font='Courier 12')
sg.theme_add_new('VSC Theme', vsc_theme)
sg.theme('VSC Theme')

origin_list = ['born digital', 'reformatted digital', 'digitized microfilm', 'digitized other analog']

tab1 = sg.Tab('Origin', [
    [sg.Checkbox('Enable?', enable_events=True, key='-ORIGIN_CB-')],
    [sg.Text('Born Digital or Digitized:'), sg.Combo(origin_list, readonly=True, disabled=True, background_color=alt_background, key='-BD_DIGIT-')],
    [sg.Text('Date Created:'), sg.Input(tooltip='YYYY-MM-DD, YYYY-MM, or YYYY', disabled=True, size=30, background_color=alt_background, key='-DATE_CREATED-'), sg.CalendarButton('Date Picker', format='%Y-%m-%d', disabled=True, key='-DATE_CREATED_BUTTON-')],
    [sg.Text('Created By:'), sg.Input(tooltip='This can the creator of a born digital resource or the person or organization that digitized it', disabled=True, background_color=alt_background, key='-CREATOR-')]
], key='-TAB_1-')

rights_basis_list = ['Public Domain', 'Under Copyright', 'Fair Use', 'License Agreement']

tab2 = sg.Tab('Rights', [
    [sg.Checkbox('Enable?', enable_events=True, key='-RIGHTS_CB-')],
    [sg.Text('Rights Basis:'), sg.Combo(rights_basis_list, readonly=True, disabled=True, background_color=alt_background, enable_events=True, default_value='Public Domain', key='-RIGHTS_BASIS-')],
    [sg.Text('Date Determined:', key='-DATE_DETERM_LABEL-'), sg.Input(size=27, disabled=True, background_color=alt_background, key='-DATE_DETERM-'), sg.CalendarButton('Date Picker', format='%Y-%m-%d', disabled=True, key='-DATE_DETERM_BUTTON-')],
    [sg.Text('Terms:', text_color='#6b6565', key='-RIGHTS_TERMS_LABEL-'), sg.Multiline(size=(49, 5), disabled=True, background_color=alt_background, key='-RIGHTS_TERMS-')],
    [sg.Text('Notes:'), sg.Multiline(size=(49, 5), disabled=True, background_color=alt_background, key='-RIGHTS_NOTES-')],
    [sg.Text('Determined By:'), sg.Input(size=42, disabled=True, background_color=alt_background, key='-DETERMININER-')]
], key='-TAB_2-')

action_list = ['accession', 'appraisal', 'capture', 'compiling', 'compression', 'deaccession', 'decompression', 'decryption', 'deletion', 'digital signature generation', 'digital signature validation', 'displaying', 'dissemination', 'encryption', 'execution', 'exporting', 'extraction', 'filename change', 'fixity check', 'forensic feature analysis', 'format identification', 'imaging', 'information package creation', 'information package merging', 'information package splitting', 'ingestion', 'ingestion end', 'ingestion start', 'interpreting', 'message digest calculation', 'metadata extraction', 'metadata modification', 'migration', 'modification', 'normalization', 'packing', 'policy assignment', 'printing', 'quarantine', 'recovery', 'redaction', 'refreshment', 'rendering', 'replication', 'transfer', 'unpacking', 'unquarantine', 'validation', 'virus check']

role_list = ['authorizer', 'executing program', 'implementer', 'validator']

tab3 = sg.Tab('Actions', [
    [sg.Checkbox('Enable?', enable_events=True, key='-ACTION_CB-')],
    [sg.Text('Event Type:'), sg.Combo(action_list, readonly=True, disabled=True, background_color=alt_background, key='-EVENT_TYPE-')],
    [sg.Text('Notes:'), sg.Multiline(size=(49, 5), disabled=True, background_color=alt_background, key='-EVENT_INFO-')],
    [sg.Text('Date Executed:'), sg.Input(disabled=True, size=30, background_color=alt_background, key='-DATE_EXECUTED-'), sg.CalendarButton('Date Picker', format='%Y-%m-%d', disabled=True, key='-DATE_EXECUTED_BUTTON-')],
    [sg.Text('Executed By:'), sg.Input(disabled=True, background_color=alt_background, key='-EXECUTER-')],
    [sg.Text('Role:'), sg.Combo(role_list, readonly=True, disabled=True, key='-ROLE-')]
], key='-TAB_3-')

tab_group = sg.TabGroup([
    [tab1, tab2, tab3]
], pad=((3, 3), (5, 5)), key='-TAB_GROUP-')

layout = [[sg.Text('ID CSV:'), sg.Input(size=42, background_color=alt_background, key='-CSV_PATH-'), sg.FileBrowse(file_types=(('ID List', '*.csv'),), key='-FILE_BROWSE_BUTTON-')],
    [sg.Text('Output Folder:'), sg.Input(size=35, background_color=alt_background, key='-OUTPUT-'), sg.FolderBrowse(key='-FOLDER_BROWSE_BUTTON-')],
    [sg.Text('Encoding for Output:'), sg.Combo(['XML', 'JSON'], readonly=True, key='-ENCODING-'), sg.Push(), sg.Button('GitHub Repo', button_color=('#ffaf5f', alt_background), key='-GITHUB-')],
    [tab_group],
    [sg.Button('Generate PREMIS Records', tooltip="LET'S GOOOOOOOOOO", font=big_font, key='-LETS_GOOOO-'), sg.ProgressBar(max_value=1, size=(14, 30), bar_color=('#ffaf5f', alt_background), key='-PROGRESS_BAR-'), sg.Button('About', key='-ABOUT-'), sg.Button('Exit', key='-EXIT-')],
    [sg.Text(expand_x=True, text_color='#ffaf5f', background_color=alt_background, key='-STATUS_BAR-')]
]

window = sg.Window('PREMIS Utility', layout, finalize=True, resizable=False, icon=program_icon)
window.set_min_size(window.size)
bd_digit = window['-BD_DIGIT-']
date_created = window['-DATE_CREATED-']
date_created_button = window['-DATE_CREATED_BUTTON-']
creator = window['-CREATOR-']
rights_basis = window['-RIGHTS_BASIS-']
date_determ_label = window['-DATE_DETERM_LABEL-']
date_determ = window['-DATE_DETERM-']
date_determ_button = window['-DATE_DETERM_BUTTON-']
terms_label = window['-RIGHTS_TERMS_LABEL-']
terms = window['-RIGHTS_TERMS-']
rights_notes = window['-RIGHTS_NOTES-']
determiner = window['-DETERMININER-']
event_type = window['-EVENT_TYPE-']
event_info = window['-EVENT_INFO-']
date_executed = window['-DATE_EXECUTED-']
date_executed_button = window['-DATE_EXECUTED_BUTTON-']
executer = window['-EXECUTER-']
role = window['-ROLE-']
progress_bar = window['-PROGRESS_BAR-']
status_bar = window['-STATUS_BAR-']

about_text = '''Created by: John Dewees
Version: 1.1.0
Last Updated: 2024-01-29
Email: john.dewees@rochester.edu
code4lib Slack: @John Dewees'''

while True:
    event, values = window.read()
    csv_path = values['-CSV_PATH-']
    output_folder = values['-OUTPUT-']
    encoding = values['-ENCODING-']
    bd_digit_value = values['-BD_DIGIT-']
    date_created_value = values['-DATE_CREATED-']
    creator_value = values['-CREATOR-']
    rights_basis_value = values['-RIGHTS_BASIS-']
    deter_date_value = values['-DATE_DETERM-']
    note_value = values['-RIGHTS_NOTES-']
    terms_value = values['-RIGHTS_TERMS-']
    determiner_value = values['-DETERMININER-']
    event_type_value = values['-EVENT_TYPE-']
    event_info_value = values['-EVENT_INFO-']
    date_executed_value = values['-DATE_EXECUTED-']
    executor_value = values['-EXECUTER-']
    role_value = values['-ROLE-']
    if event in (sg.WIN_CLOSED, '-EXIT-', 'Exit', 'Quit'):
        break
    if event == '-ORIGIN_CB-' and values['-ORIGIN_CB-'] == True:
        origin_enable(bd_digit, date_created, date_created_button, creator)
    if event == '-ORIGIN_CB-' and values['-ORIGIN_CB-'] == False:
        origin_disable(bd_digit, date_created, date_created_button, creator)
    if event == '-RIGHTS_CB-' and values['-RIGHTS_CB-'] == True:
        rights_enable(rights_basis, date_determ, date_determ_button, terms, rights_notes, determiner)
    if event == '-RIGHTS_CB-' and values['-RIGHTS_CB-'] == False:
        rights_disable(rights_basis, date_determ, date_determ_button, terms, rights_notes, determiner)
    if event == '-ACTION_CB-' and values['-ACTION_CB-'] == True:
        action_enable(event_type, event_info, date_executed, date_executed_button, executer, role)
    if event == '-ACTION_CB-' and values['-ACTION_CB-'] == False:
        action_disable(event_type, event_info, date_executed, date_executed_button, executer, role)
    if event == '-RIGHTS_BASIS-':
        rights_fields_toggle(rights_basis_value, terms_label, terms, date_determ_label, date_determ, date_determ_button)
    if event == '-GITHUB-':
        webbrowser.open_new_tab('https://github.com/rochester-rcl/premis-generator')
    if event == '-ABOUT-':
        sg.popup_ok(about_text, title='PREMIS Utility About')
    if event == '-LETS_GOOOO-':
        disable_all(window, event_type, event_info, date_executed, date_executed_button, executer, role, bd_digit, date_created, date_created_button, creator, rights_basis, date_determ, date_determ_button, terms, rights_notes, determiner)
        count = 0
        progress_bar.update(bar_color=('#ffaf5f', alt_background))
        id_list = create_idlist(csv_path)
        max_hand = open(csv_path, 'r')
        progress_bar.update(current_count = count, max=len(max_hand.readlines()))
        max_hand.close()
        window.refresh()
        for id in id_list:
            premis_origin_section = ''
            premis_rights_section = ''
            premis_action_section = ''
            if values['-ORIGIN_CB-'] == True:
                premis_origin_section = premis_origin_generate(id, bd_digit_value, date_created_value, creator_value)
            if values['-RIGHTS_CB-'] == True:
                premis_rights_section = premis_rights_generate(id, rights_basis_value, deter_date_value, note_value, terms_value, determiner_value)
            if values['-ACTION_CB-'] == True:
                premis_action_section = premis_action_generate(event_type_value, event_info_value, date_executed_value, executor_value, role_value, id)
            premis_header, premis_footer = generate_header_footer(id)
            premis_xml = premis_header + premis_origin_section + premis_rights_section + premis_action_section + premis_footer
            phand = open(os.path.join(output_folder, id + '.' + encoding.lower()), 'w')
            if encoding == 'JSON':
                data_dict = xmltodict.parse(premis_xml, process_namespaces=True)
                premis_json = json.dumps(data_dict, indent=4)
                phand.write(premis_json)
            else:
                phand.write(premis_xml)
            phand.close()
            count += 1
            progress_bar.update(current_count=count)
            status_bar.update(value = 'Creating: ' + id + '.' + encoding.lower())
            window.refresh()
        progress_bar.update(bar_color=('#5dd495', alt_background))
        sg.popup_ok('Created {count} PREMIS records in:\n\n{directory}\n\nPlease enjoy your newly created preservation metadata.'.format(count=count, directory=output_folder), title='Metadata Generated')
        status_bar.update(value='')
        enable_all(values, window, event_type, event_info, date_executed, date_executed_button, executer, role, bd_digit, date_created, date_created_button, creator, rights_basis, date_determ, date_determ_button, terms, rights_notes, determiner)
window.close()
