import PySimpleGUI as sg
import os.path
import traceback

DEFAULT_INPUT_FOLDER = "videos"
DEFAULT_OUTPUT_FOLDER = "output"
input_path = DEFAULT_INPUT_FOLDER
output_folder = DEFAULT_OUTPUT_FOLDER
output_path_name = ""
file_selected = False

try:
    # Get list of files in default folder
    file_list = os.listdir(DEFAULT_INPUT_FOLDER)
except:
    file_list = []

default_fnames = [
    f
    for f in file_list
    if os.path.isfile(os.path.join(DEFAULT_INPUT_FOLDER, f))
    and f.lower().endswith((".png", ".gif", ".mp4"))
]

# window layout
file_list_column = [
    [
        sg.Text("Source Folder"),
        sg.In(default_text=DEFAULT_INPUT_FOLDER, size=(25, 1), enable_events=True, key="-SRC FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=default_fnames, enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
    [
        sg.Text("Output Folder"),
        sg.In(default_text=DEFAULT_OUTPUT_FOLDER, size=(25, 1), enable_events=True, key="-OUT FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Button("Analyse Footage", key="-RUN COUNTER-")
    ],
]

result_column = [
    [sg.Text("Choose video file to analyse", size=(40, 1), key="-TOUT-")],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column, element_justification='center'),
        sg.VSeperator(),
        sg.Column(result_column),
    ]
]

window = sg.Window("People Counter", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-SRC FOLDER-":
        folder = values["-SRC FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif", ".mp4"))
        ]
        window["-FILE LIST-"].update(fnames)
        file_selected = False
    elif event == "-OUT FOLDER-":
        output_folder = values["-OUT FOLDER-"]
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-SRC FOLDER-"], values["-FILE LIST-"][0]
            )
            input_path = filename
            window["-TOUT-"].update(filename)
            basename = os.path.basename(filename)
            output_path_name = os.path.splitext(basename)[0]
            file_selected = True

        except:
            pass
    elif event == "-RUN COUNTER-":
        if file_selected:
            if output_folder == DEFAULT_OUTPUT_FOLDER:
                if not os.path.exists(DEFAULT_OUTPUT_FOLDER):
                    os.mkdir(DEFAULT_OUTPUT_FOLDER)
            output_folder = os.path.join(output_folder, output_path_name)
            print(output_folder)
            os.mkdir(output_folder)
            cli_input_strings = ("python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input ", 
                            " --output ", ".avi --output-csv ", ".csv --output-plots ")
            output_path = os.path.join(output_folder, output_path_name)
            final_input = cli_input_strings[0] + input_path + cli_input_strings[1] + output_path + cli_input_strings[2] + output_path + cli_input_strings[3] + output_path
            print(final_input)
            os.system(final_input) # insert run script here
            sg.Popup("Success!")
        else:
            sg.popup_error(f'ERROR', "Please select a file!")

window.close()
