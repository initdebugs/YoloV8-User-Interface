import PySimpleGUI as sg

def first_page_layout():
    layout = [
        [sg.Radio('Training', "RADIO1", default=True, key='training_radio')],
        [sg.Radio('Detection', "RADIO1", key='detection_radio')],
        [sg.Button('Next'), sg.Button('Cancel')]
    ]
    return layout

def training_page_layout():
    layout = [
        [sg.Radio('Object Detection', "RADIO2", default=True, key='object_detection'), sg.Radio('Segmentation', "RADIO2", key='segmentation')],
        [sg.InputText(key='yaml', readonly=True, do_not_clear=True, enable_events=True, size=(40, 1)), sg.FileBrowse('Browse YAML', file_types=(('YAML Files', '*.yaml'), ('All Files', '*.*')))],
        [sg.Radio('n', "RADIO3", default=True, key='model_n'), sg.Radio('s', "RADIO3", key='model_s'), sg.Radio('m', "RADIO3", key='model_m'), sg.Radio('l', "RADIO3", key='model_l'), sg.Radio('x', "RADIO3", key='model_x')],
        [sg.Text('Epochs:'), sg.InputText(key='epochs', size=(5, 1), do_not_clear=True, enable_events=True)],
        [sg.ProgressBar(100, orientation='h', size=(40, 20), key='progress'), sg.Text('0%', key='progress_percentage', size=(5, 1))],
        [sg.Button('Train'), sg.Button('Back'), sg.Button('Cancel')]
    ]
    return layout

def detection_page_layout():
    layout = [
        [sg.Radio('Object Detection', "RADIO2", default=True, key='object_detection'), sg.Radio('Segmentation', "RADIO2", key='segmentation')],
        [sg.InputText(key='video', readonly=True, do_not_clear=True, enable_events=True, size=(40, 1)), sg.FileBrowse('Browse Video/Image', file_types=(('Video Files', '*.mp4'), ('Image Files', '*.jpg *.jpeg *.png'), ('All Files', '*.*')))],
        [sg.InputText(key='model', readonly=True, do_not_clear=True, enable_events=True, size=(40, 1)), sg.FileBrowse('Browse Model')],
        [sg.Text('Extra options:'),sg.Listbox(['Hide labels', 'Hide confidence'], key='dropdown_options', size=(20, 2), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, enable_events=True)],
        [sg.Checkbox('Use GPU', key='gpu'), sg.Checkbox('Show', key='show')],
        [sg.Button('Process'), sg.Text('', key='status', size=(50, 1))],
        [sg.ProgressBar(100, orientation='h', size=(40, 20), key='progress'), sg.Text('0%', key='progress_percentage', size=(5, 1))],
        [sg.Button('Back'), sg.Button('Cancel')]
    ]
    return layout
