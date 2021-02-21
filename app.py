import PySimpleGUI as sg
import os.path
import traceback

inputPath = ""
outputFileName = ""
outputFolder = ""

# window layout
file_list_column = [
    [
        sg.Text("Source Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-SRC FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
    [
        sg.Text("Output Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-OUT FOLDER-"),
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
    elif event == "-OUT FOLDER-":
        outputFolder = values["-OUT FOLDER-"]
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-SRC FOLDER-"], values["-FILE LIST-"][0]
            )
            inputPath = filename
            window["-TOUT-"].update(filename)
            basename = os.path.basename(filename)
            outputFileName = os.path.splitext(basename)[0]

        except:
            pass
    elif event == "-RUN COUNTER-":
        cliInputStrings = ("python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input ", 
                          " --output ", ".avi --output-csv ", ".csv --output-plots ")
        outputPath = os.path.join(outputFolder, outputFileName)
        finalInput = cliInputStrings[0] + inputPath + cliInputStrings[1] + outputPath + cliInputStrings[2] + outputPath + cliInputStrings[3] + outputPath
        print(finalInput)
        try:
            os.system(finalInput) # insert run script here
        except Exception as e:
            tb = traceback.format_exc()
            sg.Print(f'An error happened.  Here is the info:', e, tb)
        sg.Popup("Success!")

window.close()
